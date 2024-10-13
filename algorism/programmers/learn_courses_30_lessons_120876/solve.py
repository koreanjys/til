# 우선 길이가 겹치는 구간을 2로 표시
# 한번에 각 행을 읽어오면

def solution(lines):
    i = 0  # 겹치는 유무 찾기
    overlap = 0  # 겹친 길이
    n = -100
    while n <= 100:

        # i 값이 2 이상일 때 겹친 길이 +1 씩
        if i >= 2:
            overlap += 1

        # 겹치는 구간 찾기 (i 값이 2 이상)
        if lines[0][0] == n:
            i += 1
        if lines[1][0] == n:
            i += 1
        if lines[2][0] == n:
            i += 1
        
        # end 값에서 i 값을 -1 함

        if lines[0][1] == n:
            i -= 1
        if lines[1][1] == n:
            i -= 1
        if lines[2][1] == n:
            i -= 1
        
        n += 1
    
    return overlap



# 입출력과 예
a = [[0, 1], [2, 5], [3, 9]]	# 2
b = [[-1, 1], [1, 3], [3, 9]]	# 0
c = [[0, 5], [3, 9], [1, 10]]	# 8

print(solution(a))
print(solution(b))
print(solution(c))