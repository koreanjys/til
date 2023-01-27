def solution(dots):
    # 기울기(m) 구하는 공식 = y'- y / x' - x
    # 각 점과 점마다 기울기를 구해본다.
    # 기울기가 같은 두 점이 나오면 return 1
    # 나오지 않으면 return 0
    
    for dot in dots:
        x1 = dot[0]
        x2 = dot[1]
        n = dots.index(dot)
        while len(dots) - 1 > n:





a = [[1, 4], [9, 2], [3, 8], [11, 6]]
b = [[3, 5], [4, 1], [2, 4], [5, 10]]

print(solution(a))
print(solution(b))