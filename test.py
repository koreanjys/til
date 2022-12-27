lst = []
lst_2 = []

arr = list(range(1, 5))
n = len(arr)  # n 원소의 개수
for i in range(1<<n):  # 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i&(1<<j):  # i의 j번째 원소 출력
            lst_2.append(arr[j])
    lst.append(lst_2)
    lst_2 = []
            
print(lst)

# 비트연산자 공부도 안한거로 풀려다가 머리 아파서 복붙으로 풀어버림..
