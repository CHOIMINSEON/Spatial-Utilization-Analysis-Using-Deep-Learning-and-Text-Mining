# 딥러닝과 텍스트 마이닝을 사용한 공간활용조사 방법에 관한 연구(2025)
* 비정형 데이터(이미지, 텍스트)를 수집해 공간의 방문자 수 추이, 활동 등 공간 활용을 분석하는 방법론을 제안.
* 서울시 복합문화공간 3곳을 대상으로 방법론을 적용해 공간활용조사를 진행.
* 이미지에서 객체를 검출하고, 동일 장소 관련 블로그 텍스트를 분석해 공간을 분석하고 두 데이터 간의 상관성을 확인.


### [연구 방법]
**시계열 데이터 수집(월별/일별)**
- **이미지 크롤링**: 서울 복합문화공간 3곳 네이버 이미지 수집(Selenium)
- **텍스트 크롤링**: 서울 복합문화공간 3곳 네이버 블로그 텍스트 수집 (Selenium)

**객체 검출 (YOLOv8)**
- **80개 클래스**: COCO 데이터셋 기반 객체 인식
- **Confidence Score**: 검출 신뢰도 자동 측정
- **배치 처리**: 대량 이미지 자동 분석
- **라벨 생성**: YOLO 형식 txt 파일 저장

**데이터 분석**
- **객체 집계**: 월별/범주별 객체 개수 통계
- **중복 제거**: 동일 이미지 내 객체 중복 처리
- **비율 계산**: 범주별 객체 출현 비율 산출
- **필터링**: 분석 대상 객체 선택적 추출

**텍스트 마이닝**
- **워드 클라우드**: 불용어 제거 후 시각화
- **빈도 분석**: 상위 키워드 자동 추출
- **토큰화**: NLTK 기반 단어 분리
- **CSV 변환**: 분석 결과 구조화 저장

**통계 검정**
- **상관분석**: Spearman/Pearson 상관계수 산출
- **독립성 검정**: Chi-Square/Fisher 검정
- **일치도 분석**: Cohen's Kappa 계산
- **시각화**: 분석 결과 그래프 생성
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
## Analysis Workflow
**Image Analysis**
```text
이미지 크롤링 데이터 (.jpg)
↓
1_yolov8.py → YOLOv8 객체 검출
↓
2_csv_make.py → 라벨 파일 CSV 변환
↓
3_sum_confidence.py → 객체별 집계 + confidence
↓
4_person_count.py → 사람 객체 월별 집계
↓
5_sum_object.py → 분석 대상 객체 필터링
↓
6_object_count_confidence.py → 연간 데이터 통합
↓
7_object_count_month.py → 월별 비율 계산
↓
[결과 CSV]
```
**Text Analysis**
```text
텍스트 크롤링 데이터 (.csv)
↓
txt.py / txt_month.py → 네이버 블로그 크롤링
↓
csv_sum.py → 월별 데이터 병합
↓
data_mining.py → 워드 클라우드 생성
↓
data_mining_graph.py → 단어 빈도 분석
↓
[키워드 CSV]
```
**Statistical Analysis**
```text
통계 분석 시작(검증을 위해 여러 통계 방법 적용 시도)
│
├─ 데이터 타입이 순위형인가?
│ ├─ YES → Spearman Rank Correlation ✓
│ └─ NO → 다음 단계
│
├─ 데이터 타입이 비율(연속형)인가?
│ ├─ YES → Spearman Proportion / Pearson
│ │ └─ 정규성 확인 → Spearman 선택 ✓
│ └─ NO → 다음 단계
│
├─ 범주형 데이터의 독립성 검정?
│ ├─ 전체 교차분석 → Chi-Square (Cross) ✓
│ ├─ 범주별 분석 → Chi-Square (Categorical) ✓
│ └─ 소표본 데이터 → Fisher's Exact (참고용)
│
└─ 분류 일치도 측정?
├─ 범주형 일치도 → Cohen's Kappa ✓
└─ 순위 일치 비율 → Pairwise Comparison ✓
```
---
### [공간별 데이터 분류]
<img width="1104" height="277" alt="image" src="https://github.com/user-attachments/assets/e3b1c411-28f5-49d9-a643-87033c287c50" />
<img width="1104" height="277" alt="image" src="https://github.com/user-attachments/assets/e3b1c411-28f5-49d9-a643-87033c287c50" />

### 정량적 결과
- 이미지-텍스트 간 상관계수 (r) 산출
- 통계적 유의성 검증 (p-value)
- 월별 시계열 패턴 도출

### 정성적 결과
- 공간 활용 특성의 시각-언어 일치성 검증
- 데이터 기반 공간 활용 유형 분류 체계 제시
- 멀티모달 데이터 분석 방법론 제안
