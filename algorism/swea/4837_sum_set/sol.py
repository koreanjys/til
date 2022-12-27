import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = tuple(map(int, (input().split())))

    lst = []
    lst_2 = []

    arr = list(range(1, 13))
    n = len(arr)  # n 원소의 개수
    for i in range(1 << n):  # 부분 집합의 개수
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번째 원소 출력
                lst_2.append(arr[j])
        lst.append(lst_2)
        lst_2 = []

    lst = list(filter(lambda e: len(e) == N, lst))
    cnt = len(list(filter(lambda e: sum(e) == K, lst)))
    print(f'#{tc} {cnt}')
