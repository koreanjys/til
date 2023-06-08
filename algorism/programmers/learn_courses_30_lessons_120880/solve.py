def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(x - n), -x))
    return answer

a = [1, 2, 3, 4, 5, 6]
b = [10000,20,36,47,40,6,10,7000]

print(solution(a, 4))
print(solution(b, 30))