import os
import pandas as pd

directory = 'C:/object/yolov8/txt/2차/성수연방'
total_rows = 0

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        num_rows = len(df)
        total_rows += num_rows
        print(f"{filename}: {num_rows}개의 행")

print(f"\n총 행 수: {total_rows}")
