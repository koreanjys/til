###################################################################################################################################################
# 필요한 라이브러리 불러오기
###################################################################################################################################################

# python과 mysql 연동을 위한 엔진
from sqlalchemy import create_engine

# mysql의 스키마
from sqlalchemy import MetaData

# 테이블 조회를 위한 모듈들
from sqlalchemy import Table, Column, Integer, String, DateTime, SmallInteger, BigInteger, ForeignKey

# 컬럼 타입을 정의하기 위한 모듈
from sqlalchemy.dialects import mysql

# 컬럼 타입을 정의하기 위한 모듈
from sqlalchemy.types import VARCHAR, INTEGER, DATETIME

# 데이터를 편집하기 위한 라이브러리
import pandas as pd

###################################################################################################################################################



###################################################################################################################################################
# Mysql과 연동할 engine 정의
###################################################################################################################################################

# db_info.txt 파일을 읽어온다.
with open('db_info.txt', 'r', encoding='utf-8') as f:
    db_info = list(map(lambda x: x.strip(), db_info := f.readlines()))
# db_info.txt 값을 대입해 Mysql과 연결한다.
engine = create_engine(f'mysql://{db_info[1]}:{db_info[2]}@{db_info[3]}:{db_info[4]}/{db_info[5]}')

# 데이터베이스 스키마 정의
metadata = MetaData(bind=engine)

###################################################################################################################################################



###################################################################################################################################################
# sources 테이블 생성 
###################################################################################################################################################

sources = Table(
    'sources',  # 테이블 명
    metadata,  # 데이터베이스 스키마

    # 컬럼 정의
    # Column('컬럼명', 타입, 특이사항)
    Column('source_id', mysql.INTEGER(20), primary_key=True), 
    Column('event_type', mysql.INTEGER(1), nullable=False),
    Column('class_type', mysql.INTEGER(1), nullable=False),
    Column('addr', String(100)),
    Column('url', String(900), nullable=False),
    Column("img_tag", String(900)),
    Column("enter_url_tag", String(900)),
    Column("page_tag", String(900)),
    Column("title_tag", String(900)),
    Column("overview_tag", String(900)),
    Column("event_date_tag", String(900)),
    Column("playtime_tag", String(900)),
    Column("place_tag", String(900)),
    Column("addr_tag", String(900)),
    Column("organizer_tag", String(900)),
    Column('superviser_tag', String(900)),
    Column("sponsor_tag", String(900)),
    Column("pay_tag", String(900)),
    Column("homepage_tag", String(900)),
    Column("tel_tag", String(900)),
    Column("sns_tag", String(900)),
    Column("cycles", mysql.INTEGER(1), nullable=False),
    Column("is_activated", mysql.INTEGER(1), nullable=False),
    Column("insert_date", DateTime, nullable=False),
    Column("insert_name", String(20), nullable=False),
    Column("update_date", DateTime, nullable=False),
    Column("update_name", String(20), nullable=False),
    Column("crawling_date", DateTime),
    
)
###################################################################################################################################################



###################################################################################################################################################
# events table 생성 
###################################################################################################################################################

# df 변수에 tables.xlsx 파일의 events 테이블 설계를 불러옴
# pd.read_excel('엑셀파일명', usecols=사용할 컬럼 범위, skiprows=무시할 행 수, nrows=사용할 행 수, na_values=결측값 처리)
df = pd.read_excel('tables.xlsx', usecols=range(1, 10), skiprows=39, nrows=22, na_values='')


# 불러온 테이블 설계의 Columns의 타입을 ORM에 맞게 변경
df['컬럼 타입'] = df['컬럼 타입'].str.replace('int', 'INTEGER')
df['컬럼 타입'] = df['컬럼 타입'].str.replace('varchar', 'VARCHAR')
df['컬럼 타입'] = df['컬럼 타입'].str.replace('datetime', 'DATETIME')


# vals_1에 기본적으로 생성해야 할 pk와 fk 정의
vals_1 = [
    Column('event_id', mysql.INTEGER(20), primary_key=True),  # 기본적으로 생성해야 하는 pk
    Column('source_id', mysql.INTEGER(20), ForeignKey('sources.source_id'))  # fk 정의 ForeignKey('테이블명.컬럼명')
]

# vals_2에 events 테이블의 columns 정의 (vals_1 값과 합칠것)
vals_2 = []

for i in range(2, df.shape[0]):
    
    # 불러온 tables.xlsx의 events 테이블 설계 df를 읽어서 columns 정의
    
    # 테이블 컬럼 명
    col_name = df['컬럼'][i]

    # 테이블 컬럼 타입
    col_type = df['컬럼 타입'][i].split('(')[0]  # 테이블 설계의 필요없는 문자열 제거 후 새롭게 타입 정의
    if '(' in df['컬럼 타입'][i]:  # 괄호가 있는건 걷어냄
        col_val = int(df['컬럼 타입'][i].split('(')[1].rstrip(')'))  # 테이블 설계의 필요없는 문자열 제거 후 새롭게 타입 정의

    val = Column(df['컬럼'][i], getattr(mysql, col_type)(col_val))  # column 타입을 정의
    vals_2.append(val)  # 정의 된 컬럼을 vals_2에 추가

# vals_1과 vals_2 정의된 컬럼들을 합침
vals = vals_1 + vals_2

# 만들어진 컬럼들(vals)를 events 테이블에 담기
events = Table(
    'events',
    metadata,
    *vals
)

# Mysql에 테이블 생성
metadata.create_all(engine)

###################################################################################################################################################



###################################################################################################################################################
# sources table에 sources.xlsx 엑셀 내용을 적용
###################################################################################################################################################

# tables.xlsx 불러와서 sources_df 에 저장
sources_df = pd.read_excel('tables.xlsx', usecols=range(1, 10), skiprows=4, nrows=28)

# columns 타입을 ORM에 맞게 수정
sources_df['컬럼 타입'] = sources_df['컬럼 타입'].str.replace('bigint', 'INTEGER')
sources_df['컬럼 타입'] = sources_df['컬럼 타입'].str.replace('int', 'INTEGER')
sources_df['컬럼 타입'] = sources_df['컬럼 타입'].str.replace('varchar', 'VARCHAR')
sources_df['컬럼 타입'] = sources_df['컬럼 타입'].str.replace('datetime', 'DATETIME')

# 빈 딕셔너리 생성
dtype = {}

# 엑셀 파일의 값들을 DB에 설정한 컬럼 타입에 맞게 수정 => dtype 빈 딕셔너리에 정의한 타입을 담기
for i in range(1, sources_df.shape[0]):
    dtype[sources_df['컬럼'][i]] = eval('mysql.' + sources_df['컬럼 타입'][i])


# sources.xlsx 파일을 읽어와서 ss_df 변수에 저장
ss_df = pd.read_excel('sources.xlsx', index_col='source_id')

# ss_df 변수에 저장된 것을 Mysql에 저장
ss_df.to_sql(name='sources', con=engine, if_exists='append', index=False, dtype=dtype)

print('Tables 생성 완료')
###################################################################################################################################################