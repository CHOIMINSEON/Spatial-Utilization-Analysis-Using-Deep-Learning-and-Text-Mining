# Cohen's Kappa (코헨스 카파)
from sklearn.metrics import cohen_kappa_score

# 데이터 준비 (이미지 순위와 텍스트 순위)
rank_data = {
    "문화_이미지": [2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1],
    "문화_텍스트": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    "휴식_이미지": [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2],
    "휴식_텍스트": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
    "지역_이미지": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    "지역_텍스트": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
}

# "문화", "휴식", "지역"에 대해 Cohen's Kappa 계산
for category in ["문화", "휴식", "지역"]:
    image_rank = rank_data[f"{category}_이미지"]
    text_rank = rank_data[f"{category}_텍스트"]
    
    # Cohen's Kappa 계산
    kappa_score = cohen_kappa_score(image_rank, text_rank)
    
    # 결과 출력
    print(f"Cohen's Kappa ({category}): {kappa_score:.4f}")
