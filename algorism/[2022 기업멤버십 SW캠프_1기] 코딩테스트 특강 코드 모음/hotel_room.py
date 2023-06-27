from itertools import permutations, combinations
from functools import cmp_to_key

def solution(k, room_number):
    answer = []

    for num in room_number:
        _num = num
        while _num in answer:
            _num += 1
        answer.append(_num)
    
    return answer



'''
k = 방 개수

rooms = {}


'''

def solve(k, room_number):
    answer = []

'''
2차원 평면 위 
N = 점 개수
점 (x, y) 좌표

1. y좌표 오름차순 정렬

2. y좌표가 같으면 x좌표 증가하는 순으로 좌표 정렬
'''

N_list = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]

# 정렬 후 값 [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]

# N_list = sorted()

help(sorted)
