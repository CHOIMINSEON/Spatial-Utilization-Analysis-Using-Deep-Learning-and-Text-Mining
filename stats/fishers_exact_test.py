# Fisher's Exact Test (피셔의 정확검정)
import numpy as np
from scipy.stats import fisher_exact

# 데이터
rank_data = {
    "문화_이미지": [2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1],
    "문화_텍스트": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    "휴식_이미지": [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2],
    "휴식_텍스트": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
    "지역_이미지": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    "지역_텍스트": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
}

# 피셔의 정확검정을 각 카테고리별로 수행
for category in ["문화", "휴식", "지역"]:
    # 이미지와 텍스트 순위 데이터
    image_rank = rank_data[f"{category}_이미지"]
    text_rank = rank_data[f"{category}_텍스트"]
    
    # 상위(1)와 하위(2, 3)를 구분하여 2x2 교차표 생성
    image_rank_binary = [1 if x == 1 else 0 for x in image_rank]  # 1위(상위) = 1, 나머지 = 0
    text_rank_binary = [1 if x == 1 else 0 for x in text_rank]    # 1위(상위) = 1, 나머지 = 0
    
    # 2x2 교차표 만들기
    contingency_table = np.array([
        [sum((np.array(image_rank_binary) == 1) & (np.array(text_rank_binary) == 1)),  # (상위, 상위)
         sum((np.array(image_rank_binary) == 1) & (np.array(text_rank_binary) == 0))], # (상위, 하위)
        [sum((np.array(image_rank_binary) == 0) & (np.array(text_rank_binary) == 1)),  # (하위, 상위)
         sum((np.array(image_rank_binary) == 0) & (np.array(text_rank_binary) == 0))]  # (하위, 하위)
    ])
    
    # 피셔의 정확검정 실행
    _, p_value = fisher_exact(contingency_table)
    
    # 결과 출력
    print(f"피셔의 정확검정 결과 ({category}):")
    print(f"p-값: {p_value:.4f}\n")
