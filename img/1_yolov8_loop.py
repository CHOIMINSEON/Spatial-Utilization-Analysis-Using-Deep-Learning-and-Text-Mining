import os

# 처리할 이름 목록
names = ["Coex", "Gyeongbokgung", "NamsanSeoulTower", "SeoulForest", "TheHyundai", "YeouidoHangangPark"]

for name in names:
    for i in range(1, 13):
        # i를 2자리 숫자로 변환 (01, 02, ..., 12)
        num = str(i).zfill(2)

        # YOLOv8 실행 명령어
        command = f"yolo predict model=yolov8x.pt source=\"C:/object/yolov8/2022_date/{name}/2022-{num}/*.jpg\" save_txt save_conf"

        # 명령어 실행
        os.system(command)
