# Stack & Queue & Deque

## 1. 스택 Stack

- 스택이란, 한쪽에서만 자료를 넣고 빼는 후입선출 LIFO(Last In First Out)형식의 선형 자료구조.

- 영단어 뜻과 같이 '쌓는다'는 뜻.

- "top"으로 정한 곳을 통해서만 들어가고 나온다.

- 박스 쌓기에 비유하자면, 아래에서 위로 쌓고, 치울 때는 맨 위에 박스부터 치운다. 
![Stack 이미지](https://velog.velcdn.com/images%2Ffalling_star3%2Fpost%2F79f0c606-6710-4452-a82c-b0e2abbf4b1a%2F%EC%BA%A1%EC%B2%98.JPG)

- 스택의 연산은 append(삽입), pop(삭제)가 있다.
- 코드로 보면 아래와 같다.
```
stack_list = []

stack_list.append(1)  # [1]
stack_list.append(2)  # [1, 2]
stack_list.append(3)  # [1, 2, 3]

stack_list.pop()  # [1, 2]
stack_list.pop()  # [1]
stack_list.pop()  # []
```

## 2. 큐 Queue

- 큐는 한 쪽에서 삽입 작업이 일어나고, 다른 한 쪽에서는 삭제 작업이 일어나는 선입선출 FIFO(First In First Out)형식의 선형 자료구조이다.

- 영단어 뜻인 "줄서기"와 같다.

- "top"으로 정한 곳을 통해서만 삽입과 삭제가 이루어지는 스택과는 달리, 큐는 한쪽에서는 삽입 작업이 일어나고, 다른 쪽에서 삭제 작업이 일어난다.

- 삽입 연산만 일어나는 곳을 리어(rear), 삭제 연산만 일어나는 곳을 프론트(front) 라고 한다.

- 리어에서 동작하는 삽입 연산을 인큐(enQueue), 프론트에서 동작하는 삭제 연산을 디큐(dnQueue)라고 한다.

- 자동차들이 터널을 줄지어 나간다고 생각하고 아래 그림을 보자.
![Queue 이미지](https://velog.velcdn.com/images%2Ffalling_star3%2Fpost%2F306aab5f-b742-4687-8d53-ab5a45b24c24%2F241.JPG)

- 큐의 연산은 collections 모듈의 deque를 쓰는게 좋다.(연산 수 최적화를 위해)

- append() : 오른쪽에서 데이터를 삽입

- appendleft() : 왼쪽에서 데이터를 삽입

- pop() : 오른쪽에서 데이터 삭제

- popleft() : 왼쪽에서 데이터 삭제

- 코드로 보면 아래와 같다.
```
from collections import deque

queue_list = deque()  # deque 구조 리스트 생성 deque([])

queue_list.append(1)  # deque([1])
queue_list.append(2)  # deque([1, 2])
queue_list.append(3)  # deque([1, 2, 3])

queue_list.popleft()  # deque([2, 3])
queue_list.popleft()  # deque([3])
queue_list.popleft()  # deque([])
```
- 위 코드와 같이 한 방향으로 들어가고 반대 반향으로 나가는 구조. 반대 반향으로 해도 된다.(appendleft와 pop으로)

## 3. 덱 Dequeue

- 덱이란, 양쪽에서 삽입과 삭제가 가능한 구조이며, 스택과 큐의 연산을 모두 지원한다.

![Dequeue 이미지](https://velog.velcdn.com/images%2Ffalling_star3%2Fpost%2F10df11e7-f1b7-4e8d-ae57-7224ab2af1fa%2F2.JPG)

- Scroll : 입력 제한 덱 (입력이 한쪽에서만 발생하고, 출력은 양쪽에서 일어날 수 있음)

- Shelf : 출력 제한 덱 (입력은 양쪽에서 일어나고, 출력은 한쪽에서 일어나도록 제한)

- 덱의 연산 역시 큐 연산과 마찬가지로 collections 모듈에서 제공하는 deque 클래스로 구현 가능

- 코드로 살펴보자.
```
from collections import deque

queue = deque()  # deque([])

queue.append(1)  # deque([1])
queue.append(2)  # deque([1, 2])
queue.append(3)  # deque([1, 2, 3])

queue.pop()      # deque([1, 2])
queue.pop()      # deque([1])
queue.pop()      # deque([])
```
