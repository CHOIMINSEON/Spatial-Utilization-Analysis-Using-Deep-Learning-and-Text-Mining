import os
import pandas as pd

# 디렉토리 경로
directory = r'C:/object/yolov8/txt/2차/코엑스'

# 모든 CSV 파일의 내용을 담을 빈 리스트
all_data = []

# 디렉토리 내의 모든 파일에 대해 반복
for filename in os.listdir(directory):
    if filename.endswith(".csv"):  # CSV 파일인 경우만 처리
        filepath = os.path.join(directory, filename)
        
        # CSV 파일을 DataFrame으로 읽기 (헤더는 제목으로 고정된 'Title')
        data = pd.read_csv(filepath, header=0)
        
        # 'Title'을 포함한 내용을 리스트에 추가
        all_data.append(data)  # 'Title'을 포함한 내용 추가

# 모든 데이터를 하나의 DataFrame으로 병합
merged_data = pd.concat(all_data, ignore_index=True)

# 합쳐진 데이터를 CSV 파일로 저장 (이전과 같은 경로에 파일 생성)
merged_data.to_csv(os.path.join(directory, 'C:/object/yolov8/txt/2차/코엑스.csv'), index=False)
