import pandas as pd
import matplotlib.pyplot as plt
import sys
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from matplotlib import font_manager, rc
from wordcloud import WordCloud

# NLTK의 불용어 다운로드
nltk.download('punkt')

# Specify the font for Matplotlib to support Korean characters
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

text_file_path = 'C:/object/yolov8/txt/더현대서울.txt'  # 텍스트 파일의 경로를 적절하게 수정하세요.

# 텍스트 파일 열기
with open(text_file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

sys.stdout.reconfigure(encoding='utf-8')

# 사용자 정의 불용어 목록 정의
#코엑스
#custom_stopwords = ["코엑스점", "한", "더", "정보", "참가", "주", "페어", "좋은", "기록", "리뷰", "강남", "코엑스", "삼성 코엑스", "후기", "일상", "삼성역", "삼성동", "서울", "2022년", "feat", "주간일기", "주간", "일기", "챌린지", "블챌", "및", "방문", "추천", "내돈내산", "삼성"]
#더현대서울
custom_stopwords = ["오늘의","더","한","그리고","내","곳","나의","주","첫","좋은","수","있는","전시","여행","부동산","뉴스","아파트","여의도", "더현대서울","더현대","더","현대","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산","그리고"]
#상상마당
#custom_stopwords = ["홍대","상상마당","이재명","윤석열","KT","G","합정역","홍대입구역","연남동","상수","합정","홍대점","홍","대","상수역","서교동","마지막","일정","수","대선","대통령","좋은","유세","후보","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
#안녕인사동
#custom_stopwords = ["프리미어","곳","좋은","한국의","이야기","안국역","안녕","안녕인사동","종로","인사동","익선동","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
#성수연방
#custom_stopwords = ["핫플","성수","성수역","성수동","성수연방","연방","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
#타임스퀘어
#custom_stopwords = ["더","한","그리고","내","곳","나의","주","첫","영등포점","신세계백화점","맛있는","타임스퀘어점","대구","여의도","영탁","좋은","주렁주렁","영등포","영등포역","타임스퀘어","영등포타임스퀘어","미국","뉴욕","뉴욕여행","New","York","여행","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]

word_tokens = word_tokenize(text_data)
filtered_text = [word for word in word_tokens if word not in custom_stopwords and word.isalpha()]

# 불용어와 특수 문자가 제외된 텍스트로 단어 빈도수 계산
word_counts = Counter(filtered_text)

# 상위 10개 단어 추출
top_words = word_counts.most_common(10)

# 데이터프레임으로 변환
df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])

# Create a pastel-toned rainbow bar graph with reversed colors
plt.figure(figsize=(12, 6))

# Add the first subplot for the bar graph
plt.subplot(1, 2, 1)
colormap = plt.get_cmap('YlGnBu')  # Choose a colormap, for example, 'YlGnBu'
# Reverse the colormap
reversed_colors = [colormap(1 - i/len(df)) for i in range(len(df))]
bars = plt.barh(df['Word'], df['Frequency'], color=reversed_colors)  # Use the reversed colormap
plt.xlabel('Frequency')
plt.ylabel('Word')
plt.title('Top 10 Words (Without Custom Stop Words and Special Characters)')

# Add data labels to the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height() / 2, f'{width}', ha='left', va='center')
plt.gca().invert_yaxis()  # Reverse the order to show the most frequent word at the top

# Add the second subplot for the word cloud
plt.subplot(1, 2, 2)
filtered_text_data = ' '.join(filtered_text)
# Specify a Korean font and scale for the word cloud (higher scale for better resolution)
wordcloud = WordCloud(width=600, height=400, background_color='white', colormap=colormap, font_path='C:/Windows/Fonts/malgun.ttf', scale=3).generate_from_frequencies(word_counts)
plt.imshow(wordcloud, interpolation='bilinear')  # Use 'bilinear' interpolation for the word cloud
plt.axis('off')
plt.title('Word Cloud (Without Custom Stop Words and Special Characters)')

plt.tight_layout()
plt.show()
