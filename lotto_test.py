from random import random
"""
import requests
from time import sleep

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1047')
data = res.json()

nums_cnt = []
for num in range(1, 46):
    nums_cnt.append([0, num])
"""
"""
num_list = {}
for drwNo in range(1, 1047 + 1):
    sleep(1)
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drwNo}')
    data = res.json()
    nums_cnt[data['drwtNo1'] - 1][0] += 1
    nums_cnt[data['drwtNo2'] - 1][0] += 1
    nums_cnt[data['drwtNo3'] - 1][0] += 1
    nums_cnt[data['drwtNo4'] - 1][0] += 1
    nums_cnt[data['drwtNo5'] - 1][0] += 1
    nums_cnt[data['drwtNo6'] - 1][0] += 1
    nums_cnt[data['bnusNo'] - 1][0] += 1

for i in nums_cnt:
    print(f'{i[1]}번 : {i[0]}개')
# data 에 딕셔너리 저장. 이 딕셔너리의 'drwtNo?' 라는 key값에 번호가 뜸
"""
# 1047회차까지 뜬 번호들 리스트는
number_list = '''
01번 : 175개,
02번 : 170개,
03번 : 164개,
04번 : 170개,
05번 : 159개,
06번 : 162개,
07번 : 164개,
08번 : 156개,
09번 : 137개,
10번 : 165개,
11번 : 166개,
12번 : 176개,
13번 : 174개,
14번 : 170개,
15번 : 163개,
16번 : 164개,
17번 : 176개,
18번 : 172개,
19번 : 158개,
20번 : 171개,
21번 : 161개,
22번 : 135개,
23번 : 143개,
24번 : 166개,
25번 : 152개,
26번 : 169개,
27번 : 177개,
28번 : 147개,
29번 : 146개,
30번 : 152개,
31번 : 165개,
32번 : 148개,
33번 : 173개,
34번 : 181개,
35번 : 162개,
36번 : 162개,
37번 : 166개,
38번 : 164개,
39번 : 172개,
40번 : 165개,
41번 : 146개,
42번 : 160개,
43번 : 181개,
44번 : 161개,
45번 : 163개'''
num_list = number_list.split(',')

ll = []
for i in num_list:
    ll.append(i[7:-1])
    

ll = list(map(int, ll))

# ll 에 인트값으로 idx 0~44까지 (로또번호 1부터 45번까지) 차례대로 등장 카운트 값이 담김 1047회까지
# 1048회 반영

ll[5] += 1
ll[11] += 1
ll[16] += 1
ll[20] += 1
ll[31] += 1
ll[38] += 1
ll[29] += 1

# 확률 계산
# 200을 기준으로 150회 등장이면 200 - 150
# l 리스트에는 1부터 45 번호가 담김
# ll 리스트에는 인덱스 0부터 인덱스 44까지 차례대로 번호1 부터 45번까지 등장한 횟수
l = list(range(1, 46))


test_1 = [1, 2, 3, 4, 5]
test_2 = [10, 10, 10, 10, 10]

