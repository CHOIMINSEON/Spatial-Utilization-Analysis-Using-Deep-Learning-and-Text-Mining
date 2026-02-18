# Spearman Rank Correlation Analysis (순위 기반 스피어만 상관분석)
import pandas as pd
from scipy.stats import spearmanr

# 데이터 준비
rank_data = {
    "문화_이미지": [2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1],
    "문화_텍스트": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    "휴식_이미지": [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2],
    "휴식_텍스트": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
    "지역_이미지": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    "지역_텍스트": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
}

# 데이터프레임 생성
rank_df = pd.DataFrame(rank_data)

# 변수 이름
variables = ["문화", "휴식", "지역"]

# 스피어만 상관분석
rank_results = {}
for var in variables:
    image_col = f"{var}_이미지"
    text_col = f"{var}_텍스트"
    spearman_corr, p_value = spearmanr(rank_df[image_col], rank_df[text_col])
    rank_results[var] = {"스피어만 상관계수": spearman_corr, "p-값": p_value}

# 결과 출력
for var, result in rank_results.items():
    print(f"{var} - 스피어만 상관계수: {result['스피어만 상관계수']:.4f}, p-값: {result['p-값']:.4f}")
