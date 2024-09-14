import os
import json
import random
from collections import OrderedDict

base_dir = os.path.dirname(os.path.abspath(__file__))

# JSON 파일 저장 위치
survey_save_dir = os.path.join(base_dir, 'cards', 'fixtures', 'survey.json')

with open(survey_save_dir, 'w', encoding="utf-8") as survey_f:
    survey_f.write('[')

    for i in range(10001):
        # Survey 모델에 데이터 삽입
        survey_file = OrderedDict()
        survey_file['model'] = 'accounts.Survey'
        survey_file['pk'] = i + 1
        survey_file['fields'] = {
            'user': i + 1,  # User 모델의 PK를 참조
            'car_owner': random.choice([0, 1]),
            'live_alone': random.choice([0, 1]),
            'student': random.choice([0, 1]),
            'baby': random.choice([0, 1]),
            'pets': random.choice([0, 1]),
            'easy_pay': random.choice([0, 1]),
            'healthcare': random.choice([0, 1]),
            'telecom': random.choice([0, 1]),
            'sports': random.choice([0, 1]),
            'shopping': random.choice([0, 1]),
            'friends': random.choice([0, 1]),
            'fitness': random.choice([0, 1]),
            'movie': random.choice([0, 1]),
            'travel_inter': random.choice([0, 1]),
            'trevel_dome': random.choice([0, 1]),
        }

        json.dump(survey_file, survey_f, ensure_ascii=False, indent='\t')
        if i != 10000:
            survey_f.write(',')
    
    survey_f.write(']')
    survey_f.close()

print(f'데이터 생성 완료 / 저장 위치: {survey_save_dir}')
