import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N은 카드 장수
    ai = list(input())  # 적힌 카드 번호
    set_ai = set(ai)
    many_card = sorted(set_ai, reverse=True, key=lambda num: (ai.count(num), num))[0]
    print(f'#{tc} {many_card} {ai.count(many_card)}')

