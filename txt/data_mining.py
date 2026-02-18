import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
import nltk
from nltk.tokenize import word_tokenize

# NLTK의 불용어 다운로드
nltk.download('punkt')

text_file_path = 'C:/object/yolov8/txt/코엑스.txt'  # 텍스트 파일의 경로를 적절하게 수정하세요.

# 텍스트 파일 열기
with open(text_file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

sys.stdout.reconfigure(encoding='utf-8')

# 사용자 정의 불용어 목록 정의
#코엑스
custom_stopwords = ["기록","리뷰","강남","코엑스", "삼성 코엑스", "후기", "일상", "삼성역", "삼성동","서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산","삼성"]  # 사용자 정의 불용어로 처리하고자 하는 단어들을 리스트로 정의합니다.
#더현대서울
#custom_stopwords = ["여의도", "더현대서울","더현대","더","현대","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산","그리고"]
#상상마당
#custom_stopwords = ["홍대","상상마당","이재명","윤석열","KT","G","합정역","홍대입구역","연남동","상수","합정","홍대점","홍","대","상수역","서교동","마지막","일정","수","대선","대통령","좋은","유세","후보","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
#안녕인사동
#custom_stopwords = ["안국역","안녕","안녕인사동","종로","인사동","익선동","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
#성수연방
#custom_stopwords = ["성수","성수역","성수동","성수연방","연방","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
#타임스퀘어
#custom_stopwords = ["영등포","영등포역","타임스퀘어","영등포타임스퀘어","미국","뉴욕","뉴욕여행","New","York","여행","리뷰","기록","후기", "일상", "서울","2022년","feat","주간일기","주간","일기","챌린지","블챌","및","방문","추천","내돈내산"]
word_tokens = word_tokenize(text_data)
filtered_text = [word for word in word_tokens if word not in custom_stopwords]

# 불용어가 제외된 텍스트로 워드 클라우드 생성
filtered_text_data = ' '.join(filtered_text)

# 워드 클라우드 생성
wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=r"C:/Windows/Fonts/malgun.ttf").generate(filtered_text_data)

# 워드 클라우드를 시각화합니다.
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 축 숨기기
plt.title('Word Cloud (Without Custom Stop Words)')
plt.show()
