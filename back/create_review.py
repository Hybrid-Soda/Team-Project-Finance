import random
import json
import os
from collections import OrderedDict

# 사용자 목록 및 카드 목록 로드
with open('./cards/fixtures/user.json', 'r', encoding='utf-8') as user_file:
    user_data = json.load(user_file)

with open('./cards/fixtures/card.json', 'r', encoding='utf-8') as card_file:
    card_data = json.load(card_file)

# 사용자와 카드의 PK 목록 추출
user_pks = [user['pk'] for user in user_data]
card_pks = [card['pk'] for card in card_data]

# 리뷰 더미 데이터 생성
review_save_dir = './cards/fixtures/review.json'
os.makedirs(os.path.dirname(review_save_dir), exist_ok=True)  # 경로가 존재하지 않으면 생성

reviews = []
N = 10000  # 생성할 리뷰 수

for i in range(N):
    review = OrderedDict()
    review['model'] = 'cards.Review'
    review['pk'] = i + 1
    review['fields'] = {
        'user': random.choice(user_pks),  # 무작위 사용자
        'card': random.choice(card_pks),  # 무작위 카드
        'rating': random.randint(2, 5),  # 2에서 5 사이의 무작위 평점
        'content': f'This is a review content for review {i + 1}',  # 임의의 리뷰 내용
        'created_at': "2024-05-22T02:59:05.894Z",
    }
    reviews.append(review)

with open(review_save_dir, 'w', encoding='utf-8') as review_f:
    json.dump(reviews, review_f, ensure_ascii=False, indent=4)

print(f'리뷰 데이터 생성 완료 / 저장 위치: {review_save_dir}')
