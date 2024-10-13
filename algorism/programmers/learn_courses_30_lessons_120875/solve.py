def solution(dots):
    # 기울기(m) 구하는 공식 = y'- y / x' - x
    # 각 점과 점마다 기울기를 구해본다.
    # 절대값으로 하면 되나?
    # (2, 5) -> (4, 3)     기울기  -2/2 = -1
    # (4, 3) -> (2, 5)     기울기  2/-2 = -1
    # 기울기가 같은 두 점이 나오면 return 1
    # 나오지 않으면 return 0
    
    # 모델링? 을 해볼까
    
    # 구조를 . . 첫번째 점 [1, 4] 를 각 점에 다 연결해보고 기울기를 뽑기
    # 뽑은 기울기를 리스트 저장? [1, -1, -2] 첫번째 점의 기울기?
    # 두번째 점은 3번째 점부터 연결해보면 되니 [-1, 1] 이런식
    # 세번째 점은 4번째랑 [1] 이렇게?
    
    # no no no 

    # 아하 근데 문제는 같은 기울기가 있으면 바로 1 리턴 하면 되는거지?
    # 그럼 set에 기울기 저장하고, x in set() 문구를 사용하면 되겠다.

    # yes

    # 기울기 gradient 를 줄여서 grad 로 하고 set으로 복수저장 할것이니 grads 로 변수명을 정하자
    grads = set()

    for dot in dots:
        x1 = dot[0]
        y1 = dot[1]
        
        # while문 조건부를 위한 n 변수 (비교를 위한 dot인덱스의 다음번 인덱스)
        n = dots.index(dot) + 1
        while len(dots) > n:
            x2 = dots[n][0]
            y2 = dots[n][1]
            m = (y2 - y1)/(x2 - x1)
            if m not in grads:
                grads.add(m)
            else:
                return 1

            n += 1            
    return 0


a = [[1, 4], [9, 2], [3, 8], [11, 6]]
b = [[3, 5], [4, 1], [2, 4], [5, 10]]

print(solution(a))
print(solution(b))