import os
import pandas as pd

# CSV 파일이 들어 있는 폴더 경로
folder_path = 'C:/object/yolov8/new/결과/csv/Y_TimeSquare/original/'
#names = ["Coex", "Hello", "KT", "Seongsu", "TimeSquare","TheHyundai"]

# 모든 CSV 파일을 읽어서 하나의 데이터프레임으로 합치기
dfs = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        dfs.append(df)

# 모든 데이터프레임을 하나로 합치기
merged_df = pd.concat(dfs, ignore_index=True)

# file_name을 기준으로 그룹화하고, class_name이 "person"인 항목의 수를 세서 그룹핑
grouped = merged_df[merged_df['class_name'] == 'person'].groupby('file_name')['class_name'].count()

# 3개 이상인 그룹의 수를 계산
count = (grouped >= 3).sum()

print(f'Class "person"이 3개 이상인 그룹의 수: {count}')
