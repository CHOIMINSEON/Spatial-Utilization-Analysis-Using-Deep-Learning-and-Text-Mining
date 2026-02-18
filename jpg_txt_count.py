import os

# 처리할 폴더 목록
#names =["Coex", "Hello", "KT", "Seongsu", "TimeSquare", "DDP", "IFC", "IPark"]
names =["SS","Y_TimeSquare"]

# 결과를 저장할 딕셔너리 초기화
folder_info = {}

# 각 폴더에 대해 순회
for name in names:
    # 폴더 경로 설정
    base_folder = f"C:/object/yolov8/new/결과/yolo/{name}"
    months = [f"2022-{str(month).zfill(2)}" for month in range(1, 13)]

    # 각 폴더별 정보를 저장할 딕셔너리 초기화
    folder_data = {}

    # 각 월별 폴더에 대해 순회
    for month in months:
        # 월별 경로 설정
        month_folder = os.path.join(base_folder, month)

        # jpg 파일 개수 구하기
        jpg_folder = os.path.join(month_folder)
        jpg_file_count = len([f for f in os.listdir(jpg_folder) if f.endswith(".jpg")])

        # labels 폴더 내 txt 파일 개수 구하기
        labels_folder = os.path.join(month_folder, "labels")
        txt_file_count = len([f for f in os.listdir(labels_folder) if f.endswith(".txt")])

        # 월별 결과를 저장
        folder_data[month] = {
            "jpg_count": jpg_file_count,
            "txt_count": txt_file_count,
        }

    # 각 폴더의 결과를 전체 결과에 저장
    folder_info[name] = folder_data

# 폴더별로 연도별 결과 합치기
combined_results = {}
for name, data in folder_info.items():
    for month, info in data.items():
        year = month.split("-")[0]  # 연도 추출
        if year not in combined_results:
            combined_results[year] = {}
        if name not in combined_results[year]:
            combined_results[year][name] = {
                "jpg_count": 0,
                "txt_count": 0,
            }
        combined_results[year][name]["jpg_count"] += info["jpg_count"]
        combined_results[year][name]["txt_count"] += info["txt_count"]

# 결과 출력
for year, folder_data in combined_results.items():
    print(f"Year: {year}")
    for folder_name, info in folder_data.items():
        print(f"Folder: {folder_name}")
        print(f"Total JPG Files Count: {info['jpg_count']}")
        print(f"Total TXT Files Count: {info['txt_count']}")
    print()
