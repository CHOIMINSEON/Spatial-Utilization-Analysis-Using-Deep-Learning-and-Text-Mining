import os
import pandas as pd

# 처리할 이름 목록
names = ["Coex", "Gyeongbokgung", "NamsanSeoulTower", "SeoulForest", "TheHyundai", "YeouidoHangangPark"]

# 입력 및 출력 경로를 names 리스트의 각 이름에 따라 반복하여 처리
for name in names:
    # 입력 경로
    input_path = rf"C:/object/yolov8/2022_date/{name}/csv/sum"
    # 출력 경로
    output_path = rf"C:/object/yolov8/2022_date/{name}/csv/sum_object"

    # 만약 출력 경로에 sum_object 폴더가 없다면 생성
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 입력 경로의 모든 파일에 대해 반복
    for filename in os.listdir(input_path):
        if filename.endswith(".csv"):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)

            # CSV 파일을 읽어옴
            df = pd.read_csv(input_file)

            # class_name 열에서 원하는 항목만 필터링
            filtered_df = df[df['class_name'].isin(['car', 'bench', 'bicycle', 'dog', 'umbrella','cell phone'])]

            # 필터링된 데이터프레임을 새로운 CSV 파일로 저장
            filtered_df.to_csv(output_file, index=False)

