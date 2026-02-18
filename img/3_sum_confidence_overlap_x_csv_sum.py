#하나씩해야함
import pandas as pd

# 처리할 이름 목록
names = ["SS"]
#"Coex", "Hello", "KT", "Seongsu", "TimeSquare", "DDP", "IFC", "IPark","TheHyundai"

# 빈 DataFrame을 생성하여 결과를 저장할 준비
combined_data = pd.DataFrame(columns=['class_name', 'file_name_count'])

for name in names:
    # 각 이름에 대한 모든 월의 데이터를 합치기 위한 빈 DataFrame
    combined_name_data = pd.DataFrame(columns=['class_name', 'file_name_count'])

    for x in range(1, 13):
        # 숫자를 2자리 수로 표현
        x_str = str(x).zfill(2)

        # CSV 파일 경로 설정
        csv_file = f'C:/object/yolov8/new/결과/csv/{name}/sum_overlap_x/2022-{x_str}.csv'

        # CSV 파일 읽기
        data = pd.read_csv(csv_file)

        # class_name 기준으로 file_name_count를 합산
        grouped_data = data.groupby('class_name')['file_name_count'].sum().reset_index()

        # 결과를 빈 DataFrame에 추가
        combined_name_data = pd.concat([combined_name_data, grouped_data])

    # 모든 월의 데이터를 합친 결과를 전체 결과에 추가하고 class_name을 기준으로 다시 합산
    combined_data = pd.concat([combined_data, combined_name_data])

    # file_name_count가 많은 순서대로 정렬
    combined_data = combined_data.groupby('class_name')['file_name_count'].sum().reset_index()
    combined_data = combined_data.sort_values(by='file_name_count', ascending=False)

    # 각 이름별로 결과를 별도의 CSV 파일로 저장
    combined_output_file = f'C:/object/yolov8/new/결과/csv/2022_{name}.csv'
    combined_data.to_csv(combined_output_file, index=False)

# 결과 출력
print("--- Combined Result ---")
print(combined_data)
