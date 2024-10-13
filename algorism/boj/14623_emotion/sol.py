import sys
sys.stdin = open('input.txt')

for i in range(2):
    b1 = int(input())
    b2 = int(input())

    result = int(b1, 2) * int(b2, 2)
    print(bin(result))