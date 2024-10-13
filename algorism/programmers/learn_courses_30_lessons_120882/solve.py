import numpy as np

def solution(score):

    # 평균 값 리스트
    means = [np.mean(s) for s in score]
    
    # 내림차순 정렬
    des_means = sorted(means, reverse=True)

    # dict 생성
    dic = {}

    # key, value 값 넣기
    for idx, m in enumerate(des_means):
        if m in dic:
            pass
        else:
            dic[m] = idx + 1

    # 점수에 맞는 등 수 매겨주기
    answer = [dic[k] for k in means]
    
    return answer
        
    

a = [[100, 0], [100, 100]]
b = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
c = [[0, 0], [0, 2], [95, 33]]


print(solution(a))
print(solution(b))
print(solution(c))