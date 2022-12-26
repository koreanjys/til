import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = tuple(map(int, input().split()))
    M_nums = list(map(int, input().split()))

    # K 충전시 갈수있는 노선 수, N 정거장 수 , M 충전기 설치된 정거장 갯수
    # M 충전가능 정거장
    n = 0  # 출발 정거장
    k = K  # 배터리
    idx = 0  # M_nums 인덱스
    cnt = 0  # 최소 충전횟수
    while True:  # 도착 전
        k -= 1  # 배터리 잔량
        n += 1  # 한칸씩 전진
        if n == N:
            break
        if n == M_nums[idx]:  # 충전소 도착하면 다음 충전소로 안내
            if idx < M - 1:
                idx += 1


            if k < N - n:  # 배터리가 종점 - 현재보다 작을때
                if k < M_nums[idx] - n or idx == M - 1:  # 배터리 잔량이 충전소까지 남은 정거장보다 작으면 현재 충전소에서 충전
                    k = K  # 배터리 충전
                    cnt += 1

                else:
                    pass

        if k == 0 and n != N:  # 배터리 떨어지면
            cnt = 0
            break
    print(f'#{tc} {cnt}')