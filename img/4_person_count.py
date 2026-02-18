import os
import pandas as pd
from datetime import datetime

# 처리할 이름 목록
names = ["SS","Y_TimeSquare"]

for name in names:
    # 입력 및 출력 경로
    input_directory = rf'C:/object/yolov8/new/결과/csv/{name}/original'
    output_directory = rf'C:/object/yolov8/new/결과/csv'
    output_file = f'{name}_person_count.csv'

    # 결과를 저장할 리스트
    person_count_list = []

    # name 폴더 내의 파일들을 순회
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_directory, filename)

            # 파일 이름에서 연도 추출
            year = filename[:4]

            # 파일 이름에서 월 추출
            month = filename[5:7]

            # 월을 영어로 변환
            month_name = datetime.strptime(month, '%m').strftime('%B')

            # CSV 파일을 DataFrame으로 읽기
            df = pd.read_csv(file_path)

            # 'class_name' 열에서 'person' 이름을 가진 행의 개수 세기
            person_count = df[df['class_name'] == 'person'].shape[0]

            # 파일 이름(월)과 개수를 리스트에 추가
            person_count_list.append({'Name': name, 'Month': month_name, 'person_Count': person_count})

    # 결과를 출력할 경로
    output_path = os.path.join(output_directory, output_file)

    # 리스트를 DataFrame으로 변환
    person_count_df = pd.DataFrame(person_count_list)

    # 결과 DataFrame을 CSV 파일로 저장
    person_count_df.to_csv(output_path, index=False)
 