import os
import json
import random
from collections import OrderedDict

base_dir = os.path.dirname(os.path.abspath(__file__))
card_file_path = os.path.join(base_dir, 'cards', 'fixtures', 'card.json')

# card.json 파일에서 카드 목록 로드
with open(card_file_path, 'r', encoding='utf-8') as card_file:
    cards_data = json.load(card_file)
    card_pks = [card['pk'] for card in cards_data]

# JSON 파일 저장 위치
recommendation_save_dir = os.path.join(base_dir, 'cards', 'fixtures', 'recommendation.json')

with open(recommendation_save_dir, 'w', encoding="utf-8") as rec_f:
    rec_f.write('[')

    for i in range(10001):
        # Recommendation 모델에 데이터 삽입
        selected_cards = random.sample(card_pks, min(10, len(card_pks)))
        recommendation_file = OrderedDict()
        recommendation_file['model'] = 'cards.Recommendation'
        recommendation_file['pk'] = i + 1
        recommendation_file['fields'] = {
            'user': i + 1,  # User 모델의 PK를 참조
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
        if i != 10000:
            rec_f.write(',')
    
    rec_f.write(']')
    rec_f.close()

print(f'데이터 생성 완료 / 저장 위치: {recommendation_save_dir}')
