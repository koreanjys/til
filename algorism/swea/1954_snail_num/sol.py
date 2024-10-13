import sys
sys.stdin = open('input.txt')

T = int(input())

cnt = 0  # 막힘카운트. 4 가되면 종료
num_cnt = 1  # 지나가면서 숫자를 남기고 감

def right(arr, c, r):  # c 는 열, r 은 행
    arr[c][r] = num_cnt  # 현재 위치에 숫자를 적기
    if r != N - 1 and arr[c][r+1] == 0:   # r 이 오른쪽 끝이 아니고, 오른쪽 값이 0 이라면
        r += 1  # 오른쪽으로 한칸 이동
    else:


for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    c = 0  # c 는 열
    r = 0  # r 은 행
