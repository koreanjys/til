# 1. a / b = 기약분수(최대공약수로 각 각 나눠줌)
# 2. b = 소인수 2, 5만 존재

def solution(a, b):
    
    default_b = b

    # 최대공약수 구하기
    while True:
        c = b
        b = a % b
        a = c  # a는 기존의 b 값을 상속받는다.
        
        if b == 0:  # 최대공약수 c 도출
            break
    
    # 분모의 소인수가 2와 5만 존재하는지
    irr = default_b // c  # 기약분수의 분모 irr
    
    if irr == 1:
        return 1  # 분모가 처음부터 1인 경우 유한소수
    
    # 2로 계속 나누고, 마지막에 5로 나눴을때 나머지가 0이 아니면 무한소수
    while True:
        if irr % 2 == 0:
            irr = irr // 2
            
            if irr == 1:  # irr 이 2로 나누어 떨어지고, 몫이 1이라면 유한소수(인수가 2(들)만 존재)
                return 1

        elif irr % 5 == 0:
            irr = irr // 5
            
            if irr == 1:  # 인수 2와 5로 전부 나누어 떨어졌다면 유한소수
                return 1

        else:
            return 2