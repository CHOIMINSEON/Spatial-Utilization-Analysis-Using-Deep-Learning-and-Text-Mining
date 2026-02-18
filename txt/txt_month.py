from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
#코엑스 영등포타임스퀘어 쌈지길 더현대서울 안녕인사동 성수연방
search = "성수연방"
search_list = search.split()

# 각 월의 일 수를 딕셔너리로 정의합니다.
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')  # 백그라운드에서 실행하도록 설정

for sl in search_list:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    for i in range(1, 13):
        print(i)
        data = pd.DataFrame(columns=['Title'])  # 새로운 데이터프레임 생성

        # 각 월의 일 수에 맞게 데이터 수집
        for x in range(1, days_in_month[i] + 1):
            date = f'2022{str(i).zfill(2)}{str(x).zfill(2)}'
            url = f'https://search.naver.com/search.naver?where=blog&query={sl}&sm=tab_opt&nso=so:r,p:from{date}to{date}'
            driver.get(url)

            prev_scroll_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)
                current_scroll_height = driver.execute_script("return document.body.scrollHeight")
                if current_scroll_height == prev_scroll_height:
                    break
                prev_scroll_height = current_scroll_height

            page_source = driver.page_source

            from bs4 import BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            titles = soup.find_all(class_='title_area')

            daily_data = []  # 각 날짜별 데이터를 저장할 리스트

            for y in titles:
                soup = BeautifulSoup(str(y), 'html.parser')
                text = soup.a.text
                daily_data.append({'Title': text})  # 각 날짜의 데이터를 리스트에 추가

            data = pd.concat([data, pd.DataFrame(daily_data)])  # 데이터프레임에 데이터 추가

        csv_file_path = f"C:/object/yolov8/txt/2022_{str(i).zfill(2)}.csv"
        data.to_csv(csv_file_path, index=False, encoding='utf-8')  # 데이터프레임을 CSV 파일로 저장
        print(f"{csv_file_path} 파일에 저장되었습니다.")

    driver.quit()
