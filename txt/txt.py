from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv
import subprocess


# 웹 드라이버 시작

#print("검색어를 입력해 주세요(공백문자로 구분)")
#search = input()
search = "안녕인사동 성수연방 타임스퀘어 동대문DDP 용산아이파크몰 IFC몰"

search_list = search.split()

for sl in search_list:
    # 크롬 드라이버 경로 설정
    # 본인 컴퓨터에 있는 드라이버 경로로 변경
    data = []

    chrome_browser = subprocess.Popen(r'C:/Program Files/Google/Chrome/Application/chrome.exe 'r'--remote-debugging-port=9222 'r'--user-data-dir="C:\Temp\chrome"')
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),options=options)

    
    for i in range(1,13):
        
        print(i)
        range_date = 31
        if (i==2):
            range_date = 28
        if (i%2 == 1):
            range_date = 31
        if(i>7 and i%2==0):
            range_date = 31
        for x in range(1,range_date+1):
            date = '2022'+str(str(i).zfill(2))+str(str(x).zfill(2))
            
            # 네이버 블로그 검색 페이지 열기
            url = 'https://search.naver.com/search.naver?where=blog&query='+sl+'&sm=tab_opt&nso=so:r,p:from'+date+'to'+date
            driver.get(url)
            prev_scroll_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                # 페이지 스크롤 다운
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                # 스크롤 후 잠시 대기
                time.sleep(1)
                
                # 현재 스크롤 위치
                current_scroll_height = driver.execute_script("return document.body.scrollHeight")
                
                # 스크롤이 더 이상 변하지 않으면 종료
                if current_scroll_height == prev_scroll_height:
                    break
                
                # 스크롤 위치 업데이트
                prev_scroll_height = current_scroll_height

            # 스크롤 완료 후 페이지 소스 가져오기
            page_source = driver.page_source

            # BeautifulSoup을 사용하여 페이지 소스 파싱
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')

            # 블로그 제목 추출
            titles = soup.find_all(class_='api_txt_lines total_tit')
            
            # 추출한 제목을 출력 또는 저장하는 코드를 추가하세요.
            # 이전 예제 코드를 참고하여 데이터를 저장하거나 출력할 수 있습니다
            for y in titles:
                
                soup = BeautifulSoup(str(y), 'html.parser')

                 #원하는 텍스트 추출
                text = soup.a.text
                data.append(text)
            

        csv_file_path = "C:/object/yolov8/txt/jeju/"+sl+".csv"

        # CSV 파일 열기 및 데이터 쓰기
    with open(csv_file_path, mode='w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
             
        # 데이터를 열(column)로 구성하여 작성
        for item in data:
            writer.writerow([item])
        print(f"데이터가 {csv_file_path} 파일로 저장되었습니다.")
        chrome_browser.terminate()

    # 웹 드라이버 종료
    driver.quit()
