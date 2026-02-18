#yolov8 반복
import os
import glob
import subprocess

folder = "C:/object/yolov8/2022_date/Gyeongbokgung"

# 폴더 내 모든 하위 폴더를 가져옴
image_folders = glob.glob(os.path.join(folder, "2022-*"))

for image_folder in image_folders:
    # 폴더 이름만 추출
    folder_name = os.path.basename(image_folder)
    
    # 결과 저장 폴더 경로 생성
    output_folder = os.path.join(folder, "output", folder_name, folder_name)
    
    # 결과 저장 폴더 생성 (이미 존재하는 경우 무시)
    os.makedirs(output_folder, exist_ok=True)
    
    # YOLOv8 실행 명령어
    command = f"yolo predict model=yolov8x.pt source=\"{image_folder}\\*.jpg\" save_txt"
    
    # 명령어 실행
    subprocess.run(command, shell=True)
