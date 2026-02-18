import pandas as pd

# 처리할 이름 목록
#names = ["Coex", "Hello", "KT", "Seongsu", "TimeSquare","TheHyundai"]
names = ["Y_TimeSquare", "SS"]

for name in names:
    for x in range(1, 13):
        # 숫자를 2자리 수로 표현
        x_str = str(x).zfill(2)

        # CSV 파일 경로 설정
        csv_file = f'C:/object/yolov8/new/결과/csv/{name}/original/2022-{x_str}.csv'
        output_file = f'C:/object/yolov8/new/결과/csv/{name}/sum_overlap_x/2022-{x_str}.csv'

        # CSV 파일 읽기
        data = pd.read_csv(csv_file)

        # class_name과 중복되지 않는 file_name 개수를 카운트
        grouped_data = data.groupby('class_name')['file_name'].nunique().reset_index()
        grouped_data.columns = ['class_name', 'file_name_count']

        # 결과를 CSV 파일로 저장
        grouped_data.to_csv(output_file, index=False)

        # 결과 출력
        print(f"--- 2022-{x_str} {name} ---")
        print(grouped_data)
