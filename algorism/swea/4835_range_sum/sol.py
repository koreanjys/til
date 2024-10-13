import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = tuple(map(int,input().split()))  # 정수의 갯수 N, 구간의 갯수 M
    a = list(map(int, input().split()))  # N개의 정수 a

    arrays = []
    for n in range(len(a)-M+1):
        arrays.append(a[n:n+M])
    arrays.sort(key=lambda array: sum(array))
    answer = sum(arrays[-1]) - sum(arrays[0])
    print(f'#{tc} {answer}')