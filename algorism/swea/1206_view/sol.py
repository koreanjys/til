import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 건물 갯수
    buildings = list(map(int, input().split()))


