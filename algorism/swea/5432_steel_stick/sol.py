import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    Q = input().strip()

    steel_laser = Q.replace('()', 'l')  # laser 를 l 로 표시
    Fes = []  # 철 재료 '('와 인덱스 값을 스택으로 쌓을 통
    steels = []
    for idx, v in enumerate(steel_laser):
        if v == '(':
            Fes.append(idx)  # 철 재료'('의 인덱스 값을 스택으로 쌓음
        elif Fes and v == ')':  # 제출 시 문제를 일으키는 구간
            fe = Fes.pop()
            fe_range = list(range(fe, idx+1))
            steels.append(fe_range)  # 철을 range list로 만들어서 리스트에 넣음

    lasers = []  # 레이저 인덱스 값을 담을 통
    cnt = len(steels)  # 철의 갯수 cnt

    for idx, l in enumerate(steel_laser):
        if l == 'l':
            lasers.append(idx)  # 레이저 인덱스 값을 담는다
    while lasers:  # 레이저를 다 소모할 때까지 철을 자른다
        l = lasers.pop()
        for steel in steels:
            if l in steel:  # 철이 레이저 범위 안이라면
                cnt += 1
    print(f'#{tc} {cnt}')