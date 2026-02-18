import pandas as pd

# 처리할 이름 목록
#names = ["Coex", "Hello","KT","Seongsu","TimeSquare","TheHyundai"]
names = ["DDP", "IFC","IPark"]

for name in names:
    for x in range(1, 13):
        # 숫자를 2자리 수로 표현
        x_str = str(x).zfill(2)

        # CSV 파일 경로 설정
        csv_file = f'C:/object/yolov8/new/결과/csv/{name}/original/2022-{x_str}.csv'
        output_file = f'C:/object/yolov8/new/결과/csv/{name}/sum/2022-{x_str}.csv'

        # CSV 파일 읽기
        data = pd.read_csv(csv_file)

        # class_name을 기준으로 그룹화하여 객체 개수와 평균 confidence 계산
        grouped_data = data.groupby('class_name').agg({'class_name': 'count', 'confidence': 'mean'})

        # 열 이름 변경
        grouped_data = grouped_data.rename(columns={'class_name': 'count', 'confidence': 'mean confidence'})

        # count를 기준으로 내림차순 정렬
        grouped_data = grouped_data.sort_values(by='count', ascending=False)

        # 결과를 CSV 파일로 저장
        grouped_data.to_csv(output_file, index=True)

        # 결과 출력
        print(f"--- 2022-{x_str} {name} ---")
        print(grouped_data)
