import os
import csv
import calendar

folder_path = r'C:/object/yolov8/new/SS'
output_folder = r'C:/object/yolov8/new/결과/csv'
csv_file = os.path.join(output_folder, 'SS_jpg.csv')

# CSV 파일 헤더 작성
header = ['Year', 'Month', 'JPG Count']
rows = []

# 폴더 탐색
for folder_name in sorted(os.listdir(folder_path)):
    if folder_name.startswith(('2022-')) and os.path.isdir(os.path.join(folder_path, folder_name)):
        year = folder_name.split('-')[0]
        month_num = int(folder_name.split('-')[1])
        month_name = calendar.month_name[month_num]
        folder_dir = os.path.join(folder_path, folder_name)
        jpg_count = sum([1 for file in os.listdir(folder_dir) if file.lower().endswith('.jpg')])
        rows.append([year, month_name, jpg_count])

# 결과를 CSV 파일로 저장
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print(f"CSV 파일 {csv_file}이 생성되었습니다.")
