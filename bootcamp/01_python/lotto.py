my_numbers = [1, 2, 3, 4, 5, 6]

jackpot_numbers = [2, 3, 4, 5, 6, 7]
bonus_number = 8

# 내가 로또 몇등이지?

"""
1등 : 6개 일치

2등 : 5개 일치 + 나머지 하나가 보너스 (2, 3, 4, 5, 6, 8)

3등 : 5개

4등 : 4개

5등 : 3개

"""

cnt = 0

for nums in my_numbers:
    if nums in jackpot_numbers:
        cnt += 1

if cnt == 6:
    print('1등 : 6개 일치')
elif cnt == 5:
    if bonus_number in my_numbers:
        print('2등 : 5개 일치 + 나머지 하나가 보너스')
    print('3등 : 5개')
elif cnt == 4:
    print('4등 : 4개')
elif cnt == 3:
    print('5등 : 3개')
else:
    print('꽝')