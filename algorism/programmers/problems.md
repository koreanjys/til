# 프로그래머스 문제들
[python tutor(link)](https://pythontutor.com/) 사이트에서 시뮬 돌려보면 좋음

## [큐 우선순위 문제(link)](https://school.programmers.co.kr/learn/courses/30/lessons/42587#)

오늘따라 공부하기 귀찮아서 대충 풂.. 다음엔 알고리즘 사고를 추가해서 수학문제 풀듯 시간복잡도를 낮춰서 풀어볼것..

```
from collections import deque

def solution(priorities, location):
    pri = []
    for idx, num in enumerate(priorities):
        pri.append((num, idx))
        
    q = deque(pri)
    cnt = 0
    while q:
        pre = max(q)[0]
        for i in range(len(q)):
            if q[0][0] != pre:
                q.rotate(-1)
            else:
                cnt += 1
                if q[0][1] == location:
                    return cnt
                q.popleft()
                break
```