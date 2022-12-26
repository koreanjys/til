import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # len(numbers)
    numbers = list(map(int, input().split()))  # 요소 N개

    comp = 0
    for num in numbers:
        if num > comp:
            comp = num
    max_num = comp

    for num in numbers:
        if num < comp:
            comp = num
    min_num = comp

    answer = max_num - min_num
    print(answer)
    print(f'#{tc} 123')