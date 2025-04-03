# rest_framework module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import *
from .models import *
from utils import *
from crawling_utils import *


User = get_user_model()


# 카드 추천
@api_view(["POST", "PUT"])
@permission_classes([IsAuthenticated])
def gen_recommend(request, username):
    card_data = filtering(request)

    if request.method == "POST":
        serializer = RecommendationSerializer(data=card_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        recommend = get_object_or_404(Recommendation, user=request.user)
        if request.user == recommend.user:
            serializer = RecommendationSerializer(recommend, data=card_data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


def create_dictionary(key):
    result = model_to_dict(get_object_or_404(Card, pk=key))
    return result


# 추천 카드 조회
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def recommend(request, username):
    user = get_object_or_404(User, username=username)
    recommend = get_object_or_404(Recommendation, user=user)
    context = {
        "content_first_card": create_dictionary(recommend.content_first_card_pk),
        "content_second_card": create_dictionary(recommend.content_second_card_pk),
        "content_third_card": create_dictionary(recommend.content_third_card_pk),
        "content_fourth_card": create_dictionary(recommend.content_fourth_card_pk),
        "content_fifth_card": create_dictionary(recommend.content_fifth_card_pk),

        "coop_first_card": create_dictionary(recommend.coop_first_card_pk),
        "coop_second_card": create_dictionary(recommend.coop_second_card_pk),
        "coop_third_card": create_dictionary(recommend.coop_third_card_pk),
        "coop_fourth_card": create_dictionary(recommend.coop_fourth_card_pk),
        "coop_fifth_card": create_dictionary(recommend.coop_fifth_card_pk),
    }
    return Response(context)


# 카드 리스트
@api_view(["GET"])
def card_list(request):
    cards = Card.objects.all().order_by('-pk')
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)


# 카드 상세
@api_view(["GET"])
def card_detail(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    serializer = CardSerializer(card)
    return Response(serializer.data)


# 관심 카드 등록 및 해제
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def favorite(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)

    if request.method == "GET":
        if request.user in card.favorite_users.all():
            is_favorite = True
        else:
            is_favorite = False
        context = {
            "is_favorite": is_favorite,
        }
        return Response(context, status=status.HTTP_200_OK)

    elif request.method == "POST":
        if request.user in card.favorite_users.all():
            card.favorite_users.remove(request.user)
            is_favorite = False
        else:
            card.favorite_users.add(request.user)
            is_favorite = True
        context = {
            "is_favorite": is_favorite,
        }
        return Response(context, status=status.HTTP_200_OK)


# 카드 리뷰 전체 조회 / 생성
@api_view(["GET", "POST"])
def review(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)

    if request.method == "GET":
        reviews = card.review_set.all().order_by("-created_at")
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        if request.user.is_authenticated:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(card=card, user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# 카드 리뷰 삭제
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def review_detail(request, card_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# 크롤링 CSV 데이터 DB에 저장
def csv_to_db(request):
    engine = create_engine("sqlite:///db.sqlite3")
    card_data = pd.read_csv("static/card_data_new.csv", encoding="cp949")
    benefit_data = pd.read_csv("static/benefit_data_new.csv", encoding="cp949")

    card_table = Card._meta.db_table
    benefit_table = Benefit._meta.db_table

    card_data.to_sql(card_table, con=engine, if_exists="append", index=False)
    benefit_data.to_sql(benefit_table, con=engine, if_exists="append", index=False)


# 카드 고릴라 셀레니움 크롤링
def card_gorilla_selenium(request):
    driver = configure_driver()
    card_writer, benefit_writer, card_file, benefit_file = open_csv_writers()

    try:
        pk = 1
        for idx in range(1, 2498):
            try:
                pk = crawl_card_detail(driver, idx, pk, card_writer, benefit_writer)
            except Exception:
                continue
    finally:
        card_file.close()
        benefit_file.close()
        driver.quit()
