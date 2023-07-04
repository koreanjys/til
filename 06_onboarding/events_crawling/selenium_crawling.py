# HTML 파싱 라이브러리 bs4
from bs4 import BeautifulSoup

# 데이터 편집 라이브러리
import pandas as pd

# Mysql과 python 연동을 위한 sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, MetaData, insert, delete, select, update

# 날짜 모듈
from datetime import datetime, date, timedelta

# 대기시간을 위한 모듈
import time

# 정규표현식을 위한 모듈
import re

# URL string 편집 라이브러리
from urllib.parse import quote_plus, urljoin

# 크롤링 라이브러리
import requests

# html 라이브러리
import html

# 진행상황을 시각화 하는 라이브러리
from tqdm.auto import tqdm

# 크롤링 라이브러리
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

# 크롬드라이버 자동 설치 라이브러리
import chromedriver_autoinstaller

# 크롬드라이버 자동 설치
chromedriver_autoinstaller.install()


###################################################################################################################################################
# selenium 옵션 정의
###################################################################################################################################################

options = webdriver.ChromeOptions()  # 옵션 정의
options.add_argument("headless")  # 크롬드라이버 창이 뜨지 않게 함. 백그라운드 실행
# options.add_argument("no-sandbox")  # docker 사용 시 보안 error문제 해결
options.add_argument("disable-gpu")  # GPU 사용 안함
options.add_argument("lang=ko-KR")  # 언어팩을 한국어로

# (중요) 유저 정보 값. 봇이 아니라는 표시
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

###################################################################################################################################################



# 크롬드라이버 실행
driver = webdriver.Chrome(options=options)


###################################################################################################################################################
# mysql과 연동하는 engine 정의
###################################################################################################################################################

# db_info.txt를 각 줄 별로 list로 읽어옴
with open('db_info.txt', 'r', encoding='utf-8') as f:
    db_info = list(map(lambda x: x.strip(), db_info := f.readlines()))

# 읽어온 db_info를 Mysql과 연동하는 engine에 대입
engine = create_engine(f'mysql://{db_info[1]}:{db_info[2]}@{db_info[3]}:{db_info[4]}/{db_info[5]}')

# metadata(스키마) 정의
metadata = MetaData(bind=engine)

# session 정의
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

###################################################################################################################################################



# 동식물 키워드 정의
animals = ['펫', '동물', '반려', '캣', '도그', '댕', '애완', '새', '곤충', '파충류', '렙타일', '냥', '묘', '견', '강아지', '고양이']
plants = ['카네이션', '달맞이꽃', '낙엽', '오이백리향', '데이지', '모란', '유채꽃', '노루발풀', '국화',
           '양귀비', '산수유', '수련', '오이꽃', '벚꽃', '왕벚나무', '민트', '버드나무', '동백꽃', '에츠나',
             '가죽나무', '산세베리아', '해오라기', '금잔화', '개나리', '억새', '모과나무', '양송이버섯', '마근',
               '수국', '백일홍', '장미나무', '이팝나무', '앵두나무', '달리아', '제라니움', '베고니아', '매화',
                 '연꽃', '진달래', '장미', '라카스', '목련', '백련', '금난초', '돈나무', '유채', '포인세티아',
                   '단잎클로버', '느티나무', '페코니아', '백년초', '안개꽃', '오트밀', '접란나무', '라벤더',
                     '바자', '왕벚꽃', '철쭉', '뮬리', '마리골드', '무궁화나무', '코스모스', '쌈박', '봉의꽃',
                       '스위트피', '찔레', '진주모란', '나팔꽃', '클레마티스', '쑥', '한련화', '라일락', '아이리스',
                         '노루풀', '포피', '단풍나무', '프리지아', '무궁화', '고구마덩굴', '빛의여왕', '양배추',
                           '개씨름꽃', '튤립', '팬지', '계단화', '산사나무', '쑥부쟁이', '민들레', '대나무',
                             '소나무', '아카시아', '호야', '백합', '난초', '제비꽃', '수선화', '패랭이꽃',
                               '백년청', '해바라기', '메타세쿼이아', '들장미', '갈대', '말린꽃', '종달새나무',
                                 '향나무', '국수나무', '솔송이', '삼나무', '솜사탕나무', '소철나무', '동백나무', '맥문동', '패랭이풀',
                                 '허브', '꽃', '나무', '정원', '숲', '식물', '화분', '온실']


# Mysql의 sources 테이블 불러오기
sources_table = Table('sources', metadata, autoload_with=engine)

# url 디코딩 방지
params = {'encoding': quote_plus('utf8')}

# sources 테이블 데이터 프레임으로 불러오기
sources_df = pd.read_sql('sources', con=engine, params=params)

# events 테이블 데이터 프레임으로 불러오기
events_df = pd.read_sql('events', con=engine, coerce_float=False)

###################################################################################################################################################
# 팝업창 닫는 함수 close_new_tabs 정의
###################################################################################################################################################
def close_new_tabs():
    time.sleep(1)
    tabs = driver.window_handles
    while len(tabs) != 1:
        driver.switch_to.window(tabs[1])
        driver.close()
        tabs = driver.window_handles
    driver.switch_to.window(tabs[0])
###################################################################################################################################################



###################################################################################################################################################
# 소스 테이블 URL에 접속하는 url_to_html 함수 정의
###################################################################################################################################################
def url_to_html(url, idx):
    
    # 요청 오류 발생 시 err_err.txt 작성 및 is_activated 값을 1로 변경
    try:
        if sources_df['is_activated'][idx] == 0:
            driver.implicitly_wait(10)
            driver.get(url)
            close_new_tabs()
        else:
            print(f"해당 source_id: {sources_df['source_id'][idx]}는 is_activated == 1 입니다.")

    except Exception as e:
        
        # err_err.txt 작성
        with open('err_err.txt', 'a', encoding='utf-8') as f:
            log = f'''
            [[시간: {datetime.now()}]] [[source_id: {sources_df["source_id"][idx]}]]
            [[url: {url}]] [[요청 결과: {str(e)[:70]}...]]\n
            '''
            f.write(log)

        # is_activated 값을 1로 변경
        stmt = update(sources_table).where(sources_table.c.source_id==sources_df['source_id'][idx]).values(is_activated=1)
        session.execute(stmt)
        session.commit()
        session.close()
###################################################################################################################################################



###################################################################################################################################################
# 매개변수 sources 테이블의 index를 받아서 img_url, enter_url을 리스트로 반환하는 함수
###################################################################################################################################################
def img_and_enter_urls(idx):
    
    urls = []  # 이미지와 상세정보 URL을 담을 빈 리스트
    cnt = 0  # 페이지를 이동 했는지 확인하기 위한 변수
    
    # 페이지 이동을 위한 반복문
    while True:
        
        # 만약 cnt가 0이면 처음 URL에 진입
        if cnt == 0:
            url = sources_df['url'][idx]  # 소스 테이블 url 가져옴
        
        # 만약 cnt가 0이 아니면
        else:
            # 만약 해당 source_id에 페이지를 넘기는 태그가 있다면
            if sources_df['page_tag'][idx]:
                
                # 다음 페이지로 이동
                try:
                    time.sleep(3)
                    click_focus = driver.find_element(By.XPATH, sources_df['page_tag'][idx])  # 페이지 태그 위치로 찾기
                    time.sleep(3)
                    driver.execute_script("arguments[0].scrollIntoView(true);", click_focus)  # 페이지 태그 위치로 스크롤 이동
                    time.sleep(3)
                    click_focus.click()  # 페이지 태그 클릭
                    time.sleep(3)
                    url = driver.current_url  # 다음 페이지로 이동 한 후, 현재 URL을 가져옴
                except:
                    break
            else:
                break

        # url_to_html 함수 호출
        url_to_html(url, idx)

        # img_urls에 이미지url 담기
        img_urls = []
        if sources_df['img_tag'][idx]:  # 이미지 태그가 있다면
            for img_url in driver.find_elements(By.CSS_SELECTOR, sources_df['img_tag'][idx]):  # 현재 페이지의 이미지를 for문으로 전부 불러옴
                if img_url.get_attribute('src'):  # src에 이미지 주소가 있다면 리스트에 담기
                    img_urls.append(img_url.get_attribute('src'))
                elif img_url.get_attribute('style'):  # style에 이미지 주소가 있다면 리스트에 담기
                    img_urls.append(img_url.get_attribute('style'))

        # enter_urls에 상세정보url 담기
        enter_urls = []
        if sources_df['enter_url_tag'][idx]:  # 상세정보 URL 태그가 있다면
            for enter_url in driver.find_elements(By.CSS_SELECTOR, sources_df['enter_url_tag'][idx]):  # 현재 페이지의 상세정보URL들을 for문으로 전부 불러옴

                # 'onclick'이라는 속성 값이 있으면 상세정보 url을 enter_urls에 담기
                if enter_url.get_attribute('onclick'):
                    enter_urls.append(enter_url.get_attribute('onclick'))
                else:
                    # href의 url을 상세정보 url에 담기
                    enter_urls.append(enter_url.get_attribute('href'))

        # enter_urls와 img_urls의 URL들을 urls 리스트에 담기
        for i, enter_url in enumerate(enter_urls):

            # img_urls이 비어있지 않다면 enter_url과 함께 담고, 비어있다면 img_url은 빈칸('') 처리
            if img_urls:
                img_enter = (img_urls[i], enter_url)
            else:
                img_enter = ('', enter_url)
            urls.append(img_enter)
        
        # 처음 URL에 들어왔으면 cnt += 1, 페이지 이동을 했다면 break
        if cnt > 0:
            break
        else:
            cnt += 1
        
    return urls
###################################################################################################################################################



###################################################################################################################################################
# tag가 있으면 파싱해서 정보를 담고, 없으면 빈 값을 반환하는 함수 정의
###################################################################################################################################################
def is_tag(tag):
    if tag:
        try:
            driver.implicitly_wait(1)
            elem = driver.find_element(By.XPATH, tag)  # 해당 tag의 값을 찾음
            
            # 현재 위치한 tag 값만 남기고 하위 tag 값은 모두 제거
            current_html = elem.get_attribute('innerHTML')  # 해당 tag의 HTML을 가져옴
            for child in elem.find_elements(By.XPATH, './/*'):  # 하위 tag 값을 모두 제거
                current_html = current_html.replace(child.get_attribute('innerHTML'), '').strip()
            
            # 문자열 처리
            current_text = html.unescape(current_html)  # 이스케이핑 된 문자열을 원상복귀
            current_text = re.sub(r"\n", "", current_text)  # 줄바꿈 제거
            current_text = re.sub(r"\t", "", current_text)  # 탭 제거
            
            
            # 줄바꿈을 위한 <br>을 남기고 모든 태그 제거
            current_text = re.sub(r"<(?!br\s*/?>).*?>", "", current_text)
            
            # source_id 8번 때문에 추가 처리("주최 : 단감" 이런식으로 값을 가져오기 때문에 처리 => "단감" 만 가져옴)
            current_text = re.sub(r"주최 : ", "", current_text)
            current_text = re.sub(r"주관 : ", "", current_text)
            current_text = re.sub(r"후원 : ", "", current_text)
            current_text = re.sub(r"전화번호 : ", "", current_text)
            
            return current_text
        except:
            return ''
    else:
        return ''
###################################################################################################################################################



###################################################################################################################################################
# source_id의 상세정보 tag를 크롤링 하는 함수 정의
###################################################################################################################################################
def crawling_detail(idx):  # 매개변수는 소스테이블 index 값
    urls = img_and_enter_urls(idx)  # img_and_enter_urls 함수를 실행해 해당 source_id의 이미지와 상세정보 url들을 가져옴
    
    # 상세 정보들을 담을 vals 리스트 정의
    vals = []
    
    # 해당 source_id의 모든 상세 정보 URL에 접속 => 상세 정보들을 가져옴
    for img_url, enter_url in tqdm(urls, desc=f"source_id {sources_df['source_id'][idx]}", leave=False):
        
        # 상세 페이지 이동
        if 'http' not in enter_url:  # http가 없으면(javascript 코드로 되어있으면)
            driver.execute_script(enter_url)  # javascript 코드 실행하여 상세페이지 접속
            close_new_tabs()  # 팝업 창 닫는 함수
        else:
            # 상세 페이지 이동
            url_to_html(enter_url, idx)  # 페이지 접속 함수
            close_new_tabs()  # 팝업 창 닫는 함수
        
        ################################## events 테이블에 담을 상세 정보들 크롤링 시작 #####################################
        source_id = sources_df['source_id'][idx]  # fk 소스 아이디
        event_type = sources_df['event_type'][idx]  # 행사 타입 (0=이벤트, 1=교육)
        class_type = 2  # 동식물 타입 정의(우선 2로 정의 후, 나중에 키워드에 따라서 0=동물 or 1=식물 변환)
        
        # img_url 전처리(순수 url만 남기기 위한 처리)        
        if '"' in img_url:  # url 외에 다양한 내용이 있다면
            extract_img_url = re.search(r'"([^"]*)"', img_url).group(1)  #  ""안에 url만 남기고 제거
            extract_img_url = urljoin(sources_df['url'][idx], extract_img_url)  # url을 완전하게 만듦
        else:  # 순수하게 img_url만 있다면 그대로 가져옴
            extract_img_url = img_url
        

        title = is_tag(sources_df['title_tag'][idx])  # 행사 제목
        
        # 몇몇 URL은 정보가 너무 적음. 그래서 overview에 "상세 정보 홈페이지 참조" 라는 문구를 넣음
        if sources_df['source_id'][idx] in [4, 13, 14, 19, 20, 21]:  # source_id 4, 13, 14, 19, 20, 21 상세 정보 부족
            overview = "상세 정보 홈페이지 참조"
        else:
            overview = is_tag(sources_df['overview_tag'][idx])  # 상세 정보
            
        
        ################# 크롤링 된 행사 날짜를 시작,종료 날짜로 분할 (종료된 행사를 처리할 때 필요) ############################
        
        event_date = is_tag(sources_df['event_date_tag'][idx])  # 행사 날짜 tag 가져옴
        
        
        # 현재 날짜 년 월 일 생성
        today = datetime.now()  # 현재 날짜, 시간
        year = today.strftime('%Y')  # 현재 년도
        month = today.strftime('%m')  # 현재 월
        day = today.strftime('%d')  # 현재 일
        
        date_list = [year, month, day]  # 현재 년, 월, 일 리스트에 담기
        
        cnt = 0  # 날짜 문자열 처리를 위한 self_switch

        # 행사 날짜 형태에 따라 처리
        # 예) 2023-01-23 ~ 2023-02-11 | 2023.01.23 - 2023.02.11 | 2023-01-23 ~ 27 | 2023.01.23 | 등등 다양한 형태
        for tilde in ['~', ' - ']:  # '~', '-' 처리
            
            # 시작날짜와 종료날짜가 같이 있다면
            if tilde in event_date:
                # tilde 기준으로 나누어 주기
                st = event_date.split(tilde)[0]  # 시작 날짜
                ed = event_date.split(tilde)[1]  # 종료 날짜

                # st 부터 숫자만 추출
                st_list = re.findall(r"[0-9]+", st)

                # st 년 월 일 온전하게 만들기
                if len(st_list) < 3:
                    st_list = date_list[:(3 - len(st_list))] + st_list

                # st를 날짜 형식으로 포맷
                st = '-'.join(st_list)
                st = datetime.strptime(st, '%Y-%m-%d').strftime('%Y-%m-%d')

                # ed 숫자만 추출
                ed_list = re.findall(r"[0-9]+", ed)

                # ed 년 월 일 온전하게 만들기
                if len(ed_list) < 3:
                    ed_list = st_list[:(3 - len(ed_list))] + ed_list

                # ed를 날짜 형식으로 포맷
                ed = '-'.join(ed_list)
                ed = datetime.strptime(ed, '%Y-%m-%d').strftime('%Y-%m-%d')

            # 시작 날짜만 있다면 (종료 날짜를 이상하게 가져온다면 else: 밑에 의심, 가져오지 않으려면 else: 밑을 cnt += 1 까지 없애고 st = event_date만 남김)
            else:
                if cnt == 1:  # ' - ' 처리
                    st = event_date  # 행사 날짜를 시작 날짜로 가져옴
                    ed = is_tag((sources_df['event_date_tag'][idx]).replace('tr[5]', 'tr[6]'))  # 종료 날짜는 현재 tag 다음 tag에 있음
                cnt += 1  # '~'처리를 끝냈다면 cnt += 1


        playtime = is_tag(sources_df['playtime_tag'][idx])  # 행사 시간
        place = is_tag(sources_df['place_tag'][idx])  # 행사 장소
        
        # addr 값을 기본적으로 갖고 있는 source_id들이 있음, 만일 없다면 크롤링
        addr = sources_df['addr'][idx] if sources_df['addr'][idx] else is_tag(sources_df['addr_tag'][idx])  # 행사 주소
        
        organizer = is_tag(sources_df['organizer_tag'][idx])  # 행사 주최
        superviser = is_tag(sources_df['superviser_tag'][idx])  # 행사 주관
        sponsor = is_tag(sources_df['sponsor_tag'][idx])  # 행사 후원
        pay = is_tag(sources_df['pay_tag'][idx])  # 행사 비용
        

        # 홈페이지는 href를 가져와야 하기 때문에 별도 처리 필요
        homepage = is_tag(sources_df['homepage_tag'][idx])  # 행사 홈페이지

        # 홈페이지 URL이 따로 없다면 현재 상세정보 URL을 홈페이지 값으로 가져옴
        if not homepage:
            homepage = driver.current_url
        
        tel = is_tag(sources_df['tel_tag'][idx])  # 행사 문의 전화번호
        sns = is_tag(sources_df['sns_tag'][idx])  # 행사 문의 이메일 등
        insert_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 행사 정보를 가져온 날짜

        crawling_info = 0  # 행사 정보 (0=처음 가져옴, 1=서비스에 적용 중 => 바로 서비스에 적용하려면 1로 변경) 
        
        # 값들을 담을 dict 정의
        val = {
            'source_id': source_id,
            'event_type': event_type,
            'class_type': class_type,
            'img_url': extract_img_url,
            'title': title,
            'overview': overview,
            'start_date': st,
            'end_date': ed,
            'playtime': playtime,
            'place': place,
            'addr': addr,
            'organizer': organizer,
            'superviser': superviser,
            'sponsor': sponsor,
            'pay': pay,
            'homepage': homepage,
            'tel': tel,
            'sns': sns,
            'insert_date': insert_date,
            'crawling_info': crawling_info
        }
        # 위에 정의한 동식물 키워드를 참조해 동식물 관련 행사만 담기
        for animal in animals:
            if animal in val['title']:  # 키워드가 동물이라면
                val['class_type'] = 0  # 동식물 분류 코드 0
        for plant in plants:
            if plant in val['title']:  # 키워드가 식물이라면
                val['class_type'] = 1  # 동식물 분류 코드 1

        if val['class_type'] < 2:  # 동식물 행사 정보만 남김
            if val['end_date']:  # 종료된 행사는 제외
                if datetime.strptime(val['end_date'], '%Y-%m-%d') > datetime.now():
                    vals.append(val)
            else:
                vals.append(val)

        driver.back()  # 페이지 뒤로가기
        time.sleep(1)  # 1초 대기
        close_new_tabs()  # 팝업 창 닫기
    
    return vals
###################################################################################################################################################



###################################################################################################################################################
# for문으로 crawling_detail 함수 호출 => sources 테이블의 모든 URL 크롤링 (크롤링 주기라면 크롤링, 아니면 그냥 넘어감)
###################################################################################################################################################

# for문을 위한 sources table의 index 길이를 sources_len으로 정의
sources_len = sources_df.shape[0]

for idx in tqdm(range(sources_len), desc="Total"):
    
    ################ 크롤링 주기 ##################

    # 처음 크롤링이라면 날짜 상관없이 크롤링
    if sources_df['crawling_date'][idx]:
        # 매 주 월요일 크롤링
        if sources_df['cycles'][idx] == 1:  # cycle 값이 1이면 매주 크롤링
            if datetime.now().weekday() == 0:  # 매주 월요일 크롤링
                pass
            else:
                continue  # 0(월요일) ~ 6(일요일)
        
        # 매 달 1일 크롤링
        elif sources_df['cycles'][idx] == 2:  # cycle 값이 2면 매달 크롤링
            if datetime.now().day == 1:  # 매달 1일 크롤링
                pass
            else:
                continue
        
        # cycle 값이 0이면 매일 크롤링 
        else:
            pass
    else:
        pass
    ##############################################
    
    # 크롤링 정보를 데이터 프레임으로 담기
    detail_df = pd.DataFrame(crawling_detail(idx))
    
    # crawling_date를 현재 시간으로 변경
    stmt = update(sources_table).where(sources_table.c.source_id==sources_df['source_id'][idx]).values(crawling_date=datetime.now())
    session.execute(stmt)
    session.commit()
    session.close()
    
    # detail_df를 events_df에 추가, 중복된 값은 제거 (title과 start_date 가 같다면 중복값 제거)
    events_df = events_df.append(detail_df, ignore_index=True)  # detail_df를 events_df에 추가
    events_df.drop_duplicates(subset=['title', 'start_date'], inplace=True)  # 중복값 제거

# mysql 저장
events_df = events_df.loc[events_df['event_id'].isna()]  # event_id 할당이 되지 않은거만 남김(새로운 행사 정보만 남김)
events_df.to_sql(name='events', con=engine, if_exists='append', index=False)  # mysql에 행사 정보 추가
# 크롬드라이버 종료
driver.quit()

# 크롤링 완료 알림
print("크롤링 완료")