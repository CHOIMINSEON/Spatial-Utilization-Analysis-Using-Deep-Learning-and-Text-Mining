# 딥러닝과 텍스트 마이닝을 사용한 공간활용조사 방법에 관한 연구(2025)
* 비정형 데이터(이미지, 텍스트)를 수집해 공간의 방문자 수 추이, 활동 등 공간 활용을 분석하는 방법론을 제안.
* 서울시 복합문화공간 3곳을 대상으로 방법론을 적용해 공간활용조사를 진행.
* 이미지에서 객체를 검출하고, 동일 장소 관련 블로그 텍스트를 분석해 공간을 분석하고 두 데이터 간의 상관성을 확인.

---
**📁 Directory Structure**
```text
Spatial-Utilization-Analysis-Using-Deep-Learning-and-Text-Mining/
├── 📂 img/ # 이미지 객체 인식 파이프라인
│ ├── 1_yolov8.py # [Step 1] YOLOv8 객체 검출 실행
│ ├── 1_yolov8_loop.py # [Step 1-2] 반복 실행 버전
│ ├── 2_csv_make.py # [Step 2] 라벨 파일 → CSV 변환
│ ├── 3_sum.py # [Step 3] 객체별 개수 집계
│ ├── 3_sum_confidence.py # [Step 3-1] confidence 포함 집계
│ ├── 3_sum_confidence_overlap_x.py # [Step 3-2] 중복 제거 집계
│ ├── 3_sum_confidence_overlap_x_csv_sum.py # [Step 3-3] 중복 제거 합계
│ ├── 4_person_count.py # [Step 4] 사람 객체 월별 집계
│ ├── 4_person_3_count.py # [Step 4-2] 사람 객체 집계 (3개 카테고리)
│ ├── 5_sum_object.py # [Step 5] 특정 객체 필터링
│ ├── 6_object_count_confidence.py # [Step 6] 연간 데이터 통합
│ └── 7_object_count_month.py # [Step 7] 월별 객체 비율 계산
│
├── 📂 txt/ # 텍스트 크롤링 및 분석
│ ├── txt.py # 네이버 블로그 크롤링 (기본)
│ ├── txt_month.py # 네이버 블로그 크롤링 (월별)
│ ├── count.py # CSV 데이터 개수 확인
│ ├── csv_sum.py # CSV 파일 병합
│ ├── data_mining.py # 워드 클라우드 생성
│ └── data_mining_graph.py # 단어 빈도 분석 및 시각화
│
├── 📂 stats/ # 통계 분석
│ ├── spearman_rank_correlation.py # 스피어만 순위 상관분석
│ ├── spearman_proportion_correlation.py # 스피어만 비율 상관분석
│ ├── pearson_correlation.py # 피어슨 상관분석
│ ├── chi_square_cross_analysis.py # 카이제곱 교차분석
│ ├── chi_square_categorical_analysis.py # 카이제곱 범주별 분석
│ ├── fishers_exact_test.py # 피셔 정확검정
│ ├── cohens_kappa.py # Cohen's Kappa (일치도)
│ └── pairwise_comparison.py # 쌍체 비교
│
├── jpg_count.py # 이미지 파일 개수 집계
├── jpg_txt_count.py # JPG/TXT 파일 개수 비교
└── README.md # 프로젝트 설명서
```
---
**Flowchart**
```text
```
---
