import os
import json
import random
from collections import OrderedDict

# 샘플 데이터 정의
first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'


def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

# card.json 파일에서 카드 목록 로드
with open('./cards/fixtures/card.json', 'r', encoding='utf-8') as card_file:
    cards_data = json.load(card_file)
    card_pks = [card['pk'] for card in cards_data]


# 사용할 dict 키 정의
dict_keys = [
    'favorite_cards',
    'username',
    'nickname',
    'email',
    'age',
    'gender',
]

# json 파일 만들기
user_file = OrderedDict()
recommendation_file = OrderedDict()

# 유저네임 리스트 생성
username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1


# JSON 파일 저장 위치
user_save_dir = './cards/fixtures/user.json'
recommendation_save_dir = './cards/fixtures/recommendation.json'
os.makedirs(os.path.dirname(user_save_dir), exist_ok=True)

with open(user_save_dir, 'w', encoding="utf-8") as user_f, open(recommendation_save_dir, 'w', encoding="utf-8") as rec_f:
    user_f.write('[')
    rec_f.write('[')

    for i in range(N):
        # 랜덤한 데이터를 삽입
        user_file['model'] = 'accounts.User'
        user_file['pk'] = i + 1
        user_file['fields'] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            'nickname': username_list[i],  # 유저 이름과 동일
            'gender': random.choice(['남자', '여자']),  # 성별
            'age': random.randint(1, 100),  # 나이
            'favorite_cards': [],
            'password': '1234',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
        }

        json.dump(user_file, user_f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            user_f.write(',')

        # Recommendation 모델에 데이터 삽입
        selected_cards = random.sample(card_pks, min(5, len(card_pks)))
        recommendation_file['model'] = 'cards.Recommendation'
        recommendation_file['pk'] = i + 1
        recommendation_file['fields'] = {
            'user': user_file['pk'],  # User 모델의 PK를 참조
            "content_first_card_pk": selected_cards[0],
            "content_second_card_pk": selected_cards[1],
            "content_third_card_pk": selected_cards[2],
            "content_fourth_card_pk": selected_cards[3],
            "content_fifth_card_pk": selected_cards[4],
            "coop_first_card_pk": selected_cards[5],
            "coop_second_card_pk": selected_cards[6],
            "coop_third_card_pk": selected_cards[7],
            "coop_fourth_card_pk": selected_cards[8],
            "coop_fifth_card_pk": selected_cards[9],
        }

        json.dump(recommendation_file, rec_f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            rec_f.write(',')
    
    user_f.write(']')
    rec_f.write(']')
    user_f.close()
    rec_f.close()

print(f'데이터 생성 완료 / 저장 위치: {user_save_dir}, {recommendation_save_dir}')