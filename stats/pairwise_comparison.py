# Pairwise Comparison (쌍체 비율 비교)
# 데이터 준비 (이미지 순위와 텍스트 순위)
rank_data = {
    "문화_이미지": [2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1],
    "문화_텍스트": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    "휴식_이미지": [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2],
    "휴식_텍스트": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
    "지역_이미지": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    "지역_텍스트": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
}

# "문화", "휴식", "지역"에 대해 순위 차이 계산 후 일치 비율 구하기
for category in ["문화", "휴식", "지역"]:
    image_rank = rank_data[f"{category}_이미지"]
    text_rank = rank_data[f"{category}_텍스트"]
    
    # 순위 차이 계산
    rank_differences = [abs(i - t) for i, t in zip(image_rank, text_rank)]
    
    # 순위 차이가 0인 경우의 비율 (일치하는 경우)
    match_ratio = rank_differences.count(0) / len(rank_differences)
    
    # 결과 출력
    print(f"순위 일치 비율 ({category}): {match_ratio * 100:.2f}%")
