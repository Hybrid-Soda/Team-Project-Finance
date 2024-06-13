# rest_framework module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

from collections import defaultdict
from accounts.models import Survey
from .serializers import *
from .models import *
import numpy as np

# 코사인 유사도 계산 함수
def cos_similarity(x, y, eps=1e-8):
    nx = x / np.sqrt(np.sum(x**2) + eps)
    ny = y / np.sqrt(np.sum(y**2) + eps)
    return np.dot(nx, ny)

User = get_user_model()

# 카드 추천
@api_view(["POST", "PUT"])
@permission_classes([IsAuthenticated])
def gen_recommend(request, username):
    benefit_dict = {
        "간편결제": 0,
        "공과금/렌탈": 1,
        "공항라운지/PP": 2,
        "교육/육아": 3,
        "교통": 4,
        "레저/스포츠": 5,
        "마트/편의점": 6,
        "배달앱": 7,
        "병원/약국": 8,
        "뷰티/피트니스": 9,
        "쇼핑": 10,
        "애완동물": 11,
        "여행/숙박": 12,
        "영화/문화": 13,
        "자동차/하이패스": 14,
        "주유": 15,
        "카페/디저트": 16,
        "통신": 17,
        "푸드": 18,
        "항공마일리지": 19,
        "항공": 20,
        "해외": 21,
    }
    BN = len(benefit_dict)

    ### 콘텐츠 기반 필터링 ###
    def update_survey_vector(survey, vector):
        mapping = {
            0: [14, 15],       # 자동차 유무
            1: [1, 6, 7],      # 자취 여부
            2: [3],            # 학생 여부
            3: [3],            # 육아 여부
            4: [11],           # 애완동물
            5: [0],            # 결제 방법
            6: [8],            # 헬스케어
            7: [17],           # 통신
            8: [5],            # 스포츠
            9: [10],           # 쇼핑
            10: [16, 18],      # 친구
            11: [9],           # 운동
            12: [13],          # 영화
            13: [19, 20, 21],  # 국외여행
            14: [4, 12]        # 국내여행
        }

        for idx, value in enumerate(survey):
            if value:
                for pos in mapping[idx]:
                    vector[pos] = 1
            elif idx == 0:
                vector[4] = 1
        return vector

    # 설문 데이터 가져오기
    survey = get_object_or_404(Survey, user=request.user)
    survey = list(model_to_dict(survey).values())[2:]
    survey_vector = update_survey_vector(survey, [0] * (BN + 1))

    # 카드별 혜택 대분류 추출 및 가공
    cards = Card.objects.all().order_by("annual_fee1")
    benefit_matrix = []  # 혜택 벡터 배열을 가지는 혜택 행렬
    for card in cards:
        benefits = card.benefit_set.all()
        benefit = [bn.title for bn in benefits]
        benefit_vector = [0] * (BN + 2)  # 코사인 유사도를 판단하기 위한 벡터 배열

        for bene in benefit:
            # 항목이 메인 대분류에 있다면 해당 위치 벡터 활성화
            if bene in benefit_dict:
                index = benefit_dict[bene]
                benefit_vector[index] = 1
            # 기타 항목이라면 기타 위치 벡터 활성화
            else:
                benefit_vector[-2] = 1
        benefit_vector[-1] = card.pk

        # 혜택 벡터
        benefit_matrix.append(benefit_vector)

    # 코사인 유사도 측정 및 내림차순 정렬
    content_similarity_vector = [
        (cos_similarity(np.array(bv[: BN + 1]), np.array(survey_vector)), idx)
        for idx, bv in enumerate(benefit_matrix)
    ]
    content_similarity_vector.sort(reverse=True)

    # 콘텐츠 기반 필터링으로 상위 5개의 카드 선택
    recommended_card_pks_content = [benefit_matrix[idx][-1] for _, idx in content_similarity_vector[:5]]


    ### 협업 필터링 ###

    # 사용자-카드 매트릭스 생성
    reviews = get_list_or_404(Review)
    user_card_matrix = defaultdict(dict)
    for review in reviews:
        user_card_matrix[review.user.id][review.card.id] = review.rating

    # 현재 사용자 정보
    my_ratings = user_card_matrix.get(request.user.id, {})
    coop_similarity_vector = []

    # 협업 필터링 유사도 계산 함수
    def calculate_coop_similarity(user_id, my_ratings, other_ratings):
        other_user = get_object_or_404(User, id=user_id)
        gender_similarity = 1 if request.user.gender == other_user.gender else 0
        age_similarity = 1 - abs(request.user.age - other_user.age) / 100

        common_cards = set(my_ratings.keys()) & set(other_ratings.keys())
        if not common_cards:
            return (gender_similarity + age_similarity) / 2

        current_user_vector = np.array([my_ratings[card] for card in common_cards])
        other_user_vector = np.array([other_ratings[card] for card in common_cards])
        recommend_similarity = cos_similarity(current_user_vector, other_user_vector)

        return (recommend_similarity + gender_similarity + age_similarity) / 3
    
    # 협업 필터링 유사도 측정 및 정렬
    for user_id, other_ratings in user_card_matrix.items():
        if user_id == request.user.id:
            continue
        similarity = calculate_coop_similarity(user_id, my_ratings, other_ratings)
        coop_similarity_vector.append((similarity, user_id))

    coop_similarity_vector.sort(reverse=True)

    # 상위 N명의 사용자를 기반으로 카드 추천
    top_n_users = [user_id for _, user_id in coop_similarity_vector[:20]]
    recommended_cards = defaultdict(list)
    for user_id in top_n_users:
        for card_id, rating in user_card_matrix[user_id].items():
            if card_id not in my_ratings:
                recommended_cards[card_id].append(rating)

    # 평균 평점이 높은 카드 선택
    recommended_cards = sorted(recommended_cards.items(), key=lambda x: np.mean(x[1]), reverse=True)
    recommended_card_pks_coop = [card_id for card_id, _ in recommended_cards[:5]]

    # 콘텐츠 기반 필터링과 협업 필터링 결과 병합
    card_data = {
        "content_first_card_pk": recommended_card_pks_content[0],
        "content_second_card_pk": recommended_card_pks_content[1],
        "content_third_card_pk": recommended_card_pks_content[2],
        "content_fourth_card_pk": recommended_card_pks_content[3],
        "content_fifth_card_pk": recommended_card_pks_content[4],

        "coop_first_card_pk": recommended_card_pks_coop[0],
        "coop_second_card_pk": recommended_card_pks_coop[1],
        "coop_third_card_pk": recommended_card_pks_coop[2],
        "coop_fourth_card_pk": recommended_card_pks_coop[3],
        "coop_fifth_card_pk": recommended_card_pks_coop[4],
    }

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


# 추천 카드 조회
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def recommend(request, username):
    user = get_object_or_404(User, username=username)
    recommend = get_object_or_404(Recommendation, user=user)
    context = {
        "content_first_card": model_to_dict(get_object_or_404(Card, pk=recommend.content_first_card_pk)),
        "content_second_card": model_to_dict(get_object_or_404(Card, pk=recommend.content_second_card_pk)),
        "content_third_card": model_to_dict(get_object_or_404(Card, pk=recommend.content_third_card_pk)),
        "content_fourth_card": model_to_dict(get_object_or_404(Card, pk=recommend.content_fourth_card_pk)),
        "content_fifth_card": model_to_dict(get_object_or_404(Card, pk=recommend.content_fifth_card_pk)),

        "coop_first_card": model_to_dict(get_object_or_404(Card, pk=recommend.coop_first_card_pk)),
        "coop_second_card": model_to_dict(get_object_or_404(Card, pk=recommend.coop_second_card_pk)),
        "coop_third_card": model_to_dict(get_object_or_404(Card, pk=recommend.coop_third_card_pk)),
        "coop_fourth_card": model_to_dict(get_object_or_404(Card, pk=recommend.coop_fourth_card_pk)),
        "coop_fifth_card": model_to_dict(get_object_or_404(Card, pk=recommend.coop_fifth_card_pk)),
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
    import pandas as pd
    from sqlalchemy import create_engine

    # 데이터베이스 연결
    engine = create_engine("sqlite:///db.sqlite3")
    # CSV 파일 읽기
    card_data = pd.read_csv("static/card_data_new.csv", encoding="cp949")
    benefit_data = pd.read_csv("static/benefit_data_new.csv", encoding="cp949")
    # 테이블 이름 가져오기
    card_table = Card._meta.db_table
    benefit_table = Benefit._meta.db_table
    # 데이터베이스에 데이터 저장 (기존 테이블을 덮어쓰려면 if_exists='replace' -> 속성까지 덮어씌움, 추가하려면 'append')
    card_data.to_sql(card_table, con=engine, if_exists="append", index=False)
    benefit_data.to_sql(benefit_table, con=engine, if_exists="append", index=False)
    return


# 카드 고릴라 셀레니움 크롤링
def card_gorilla_selenium(request):
    # 1. 브라우저 인스턴스를 생성하고 제어
    # 2. Chrome 브라우저의 실행 옵션을 설정하는 데 사용
    # 3. Selenium에서 웹 요소를 찾는 데 사용되는 위치 전략을 정의 (웹 요소 지정)
    # 4. 지정한 윈도우나 탭을 찾을 수 없을 때 발생하는 예외 처리
    from selenium import webdriver  # 1
    from selenium.webdriver.chrome.options import Options  # 2
    from selenium.webdriver.common.by import By  # 3
    from selenium.common.exceptions import (
        NoSuchWindowException,
        NoSuchElementException,
    )  # 4
    import csv

    # 크롬 옵션에 관한 인스턴스
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )  # 불필요한 에러 메세지 없애기
    chrome_options.add_argument("--start-maximized")  # 브라우저가 최대화된 상태로 실행
    chrome_options.add_argument("disable-infobars")

    # 크롬 드라이버 인스턴스
    driver = webdriver.Chrome(options=chrome_options)

    # CSV 파일 생성 (저장 경로, 쓰기 모드, 인코딩, 줄바꿈 없음으로 조정)
    static_dir = "cards/"
    csv_data1 = open(f"{static_dir}\\card_data.csv", "w", encoding="CP949", newline="")
    card_data = csv.writer(csv_data1)
    csv_data2 = open(f"{static_dir}\\benefit_data.csv", "w", encoding="CP949", newline="")
    benefit_data = csv.writer(csv_data2)

    card_data.writerow(["pk", "name", "brand", "image", "annual_fee1", "annual_fee2", "record", "type"])
    benefit_data.writerow(["card", "title", "content"])

    pk = 1
    CARD_URL = "#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div"
    BENEFIT_URL = "#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.bene_area > dl"

    # 크롤링
    for idx in range(1, 2498):
        try:
            driver.get(f"https://www.card-gorilla.com/card/detail/{idx}")
            driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')

            try:
                if driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.data_area > div.btn_wrap > div.app_btn > a.inactive > span > b"):
                    print(driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.data_area > div.btn_wrap > div.app_btn > a.inactive > span > b"))
                    continue
            except:
                pass

            # 이름
            card_name = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.data_area > div.tit > strong").text
            # 브랜드
            card_brand = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.data_area > div.tit > p").text
            # 이미지
            card_image = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.plate_area > div.card_img > img").get_attribute("src")
            # 연회비 1
            card_annual_fee1 = (driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(1) > dd.in_out > span:nth-child(1) > b").text.replace(",", "").replace("원", ""))
            # 전월 실적
            card_record = (driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(2) > dd > b").text.replace(",", "").replace("원", ""))
            # 연회비 2
            try:
                card_annual_fee2 = (driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(1) > dd.in_out > span:nth-child(2) > b").text.replace(",", "").replace("원", ""))
            except NoSuchElementException:
                card_annual_fee2 = None
            # 타입
            try:
                card_type = driver.find_element(By.CSS_SELECTOR, f"{CARD_URL} > div.bnf2 > dl:nth-child(3) > dd > span").text
            except NoSuchWindowException:
                card_type = None

            card_data.writerow([pk, card_name, card_brand, card_image, card_annual_fee1, card_annual_fee2, card_record, card_type])

            # 혜택
            benefit_name = driver.find_elements(By.CSS_SELECTOR, f"{BENEFIT_URL} > dt > p")
            # 혜택 내용
            benefit_content = driver.find_elements(By.CSS_SELECTOR, f"{BENEFIT_URL} > dt > i")

            for i in range(len(benefit_name)):
                bnf_name = benefit_name[i].text
                bnf_content = benefit_content[i].text
                benefit_data.writerow([pk, bnf_name, bnf_content])
            pk += 1

        except:
            continue

    driver.quit()
