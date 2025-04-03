from django.shortcuts import get_object_or_404, get_list_or_404
from django.forms.models import model_to_dict
from collections import defaultdict
from accounts.models import Survey
from .serializers import *
from .models import *
import numpy as np


User = get_user_model()

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
BN = len(benefit_dict)


# 코사인 유사도 계산 함수
def get_cos_similarity(x, y, eps=1e-8):
    nx = x / np.sqrt(np.sum(x**2) + eps)
    ny = y / np.sqrt(np.sum(y**2) + eps)
    return np.dot(nx, ny)


# 설문 업데이트
def update_survey_vector(survey, vector):
    for idx, value in enumerate(survey):
        if value:
            for pos in mapping[idx]:
                vector[pos] = 1
        elif idx == 0:
            vector[4] = 1
    return vector


# 카드 혜택 행렬 생성
def get_benefit_matrix():
    cards = Card.objects.all().order_by("annual_fee1")
    benefit_matrix = []

    for card in cards:
        benefits = card.benefit_set.all()
        benefit_titles = [benefit.title for benefit in benefits]
        benefit_vector = [0] * (BN + 2)

        for title in benefit_titles:
            # 항목이 메인 대분류에 있다면 해당 위치 벡터 활성화
            if title in benefit_dict:
                index = benefit_dict[title]
                benefit_vector[index] = 1
            # 기타 항목이라면 기타 위치 벡터 활성화
            else:
                benefit_vector[-2] = 1
        
        benefit_vector[-1] = card.pk
        benefit_matrix.append(benefit_vector)
    
    return benefit_matrix


# 코사인 유사도 측정 및 내림차순 정렬
def get_similarity_vector(survey, benefits):
    vector = []
    for idx, bv in enumerate(benefits):
        x = np.array(bv[:BN+1])
        y = np.array(survey)
        score = get_cos_similarity(x, y)
        vector.append(score, idx)
    
    vector.sort(reverse=True)
    return vector


# 협업 필터링 유사도 계산
def get_coop_similarity(request, user_id, ratings, other_ratings):
    other_user = get_object_or_404(User, id=user_id)
    gender_similarity = 1 if request.user.gender == other_user.gender else 0
    age_similarity = 1 - abs(request.user.age - other_user.age) / 100
    common_cards = set(ratings.keys()) & set(other_ratings.keys())
    
    if not common_cards:
        return (gender_similarity + age_similarity) / 2

    current_user_vector = np.array([ratings[card] for card in common_cards])
    other_user_vector = np.array([other_ratings[card] for card in common_cards])
    recommend_similarity = get_cos_similarity(current_user_vector, other_user_vector)
    score = (recommend_similarity + gender_similarity + age_similarity) / 3
    return score


# 사용자-카드 평점 행렬 생성
def build_user_card_matrix():
    reviews = get_list_or_404(Review)
    matrix = defaultdict(dict)
    for review in reviews:
        matrix[review.user.id][review.card.id] = review.rating
    return matrix


# 사용자 간 협업 필터링 유사도 벡터 생성
def build_similarity_vector(current_user_id, user_card_matrix):
    my_ratings = user_card_matrix.get(current_user_id, {})
    similarity_vector = []

    for user_id, other_ratings in user_card_matrix.items():
        if user_id == current_user_id:
            continue
        similarity = get_coop_similarity(current_user_id, user_id, my_ratings, other_ratings)
        similarity_vector.append((similarity, user_id))

    similarity_vector.sort(reverse=True)
    
    return similarity_vector


def get_top_n_users(similarity_vector, n=20):
    return [user_id for _, user_id in similarity_vector[:n]]


# 추천 카드 리스트 생성
def get_recommended_cards(top_users, user_card_matrix, my_ratings):
    recommendations = defaultdict(list)
    for user_id in top_users:
        for card_id, rating in user_card_matrix[user_id].items():
            if card_id not in my_ratings:
                recommendations[card_id].append(rating)
    recommended_cards = sorted(recommendations.items(), key=lambda x: np.mean(x[1]), reverse=True)
    return recommended_cards


def create_card_data(pk_list_1, pk_list_2):
    card_data = {
        "content_first_card_pk": pk_list_1[0],
        "content_second_card_pk": pk_list_1[1],
        "content_third_card_pk": pk_list_1[2],
        "content_fourth_card_pk": pk_list_1[3],
        "content_fifth_card_pk": pk_list_1[4],

        "coop_first_card_pk": pk_list_2[0],
        "coop_second_card_pk": pk_list_2[1],
        "coop_third_card_pk": pk_list_2[2],
        "coop_fourth_card_pk": pk_list_2[3],
        "coop_fifth_card_pk": pk_list_2[4],
    }
    return card_data


def filtering(request):
    ### 콘텐츠 기반 필터링 ###
    survey = get_object_or_404(Survey, user=request.user)
    survey = list(model_to_dict(survey).values())[2:]
    survey_vector = update_survey_vector(survey, [0] * (BN + 1))
    benefit_matrix = get_benefit_matrix()
    sim_vector = get_similarity_vector(survey_vector, benefit_matrix)
    recommended_card_pks_content = [benefit_matrix[idx][-1] for _, idx in sim_vector[:5]]

    ### 협업 필터링 ###
    user_card_matrix = build_user_card_matrix()
    current_user_id = request.user.id
    my_ratings = user_card_matrix.get(request.user.id, {})
    sim_vector = build_similarity_vector(current_user_id, user_card_matrix)
    top_users = get_top_n_users(sim_vector)
    recommended_cards = get_recommended_cards(top_users, user_card_matrix, my_ratings)
    recommended_card_pks_coop = [card_id for card_id, _ in recommended_cards[:5]]

    # 콘텐츠 기반 필터링과 협업 필터링 결과 병합
    card_data = create_card_data(recommended_card_pks_content, recommended_card_pks_coop)
    return card_data