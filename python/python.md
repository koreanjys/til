# **python 학습**
## **python 설치**
1. google에서 python 검색
2. download for windows x64
3. 최신버전을 받지 않고 그 전 버전으로 다운로드
4. 설치 할때 path 체크 후 설치
5. 설치 완료 전에 disabled path? 선택 
6. 완료 후 close

## **python vscode에서 실행**
- vscode 실행 후 확장탭에서 'python' 설치
- 마찬가지로 확장탭에서 'korean language pack'설치

## **python 명령**

## **python 학습내용**
### **2022-12-14**
새로 배운걸 기록
#### **1. 단축평가**

단축평가는 확실한 값이 나오면 그 뒤에는 생략

예시1) True and True and False and True and False
      
    and 연산자는 모든게 True 일때 True를 반환하지만 하나라도 False가 있다면 False를 반환한다. 그래서 위 예시1)에서 3번째를 보면 처음으로 False가 등장한다. 그럼 컴퓨터는 뒤에는 보지 않고, 3번째 False값만 보고 결과를 False로 반환한다.

예시2) False or True or True or False or False
    
    or 연산자는 모든게 False 일때 False를 반환하고, 하나라도 True가 있으면 True를 반환한다. 고로 위 예시2)의 2번째에 True가 나왔는데 컴퓨터는 이 True를 보고 뒤에는 생략하고 True를 반환한다. 이게 단축평가다.

    아래는 설명은 생략하고 결과값만 보여주겠다.

예시3) 1 and 3 and 5 and 0 and 7 and 1

    => 0

예시4) 0 or '' or [] or 1 or False or ''

    => 1

예시5) 1 and 3 and '' and 5

    => ''

#### **2. 연산자 우선순위**
내가 잘 몰랐던것은 +와 -를 표시하는 단항연산자와 제곱(**)의 관계였다.
예를들면 -2 ** 2 이 값은 사람이 보면 4지만 컴퓨터 연산 순서는 2 ** 2 먼저 하고 그다음 -를 붙인다.
그래서 -2 ** 2를 컴퓨터가 계산하면 -4가 된다.
이럴땐 (-2) ** 2 이렇게 해주거나 

변수 x = -2 를 받아서 x ** 2를 해주는게 좋다.

#### **3. 형변환**
내가 헷갈렸던것중에 

a = '3.5' 이것을 정수로 바꿔주면 어떻게 되는가? 이다.

내 기존 지식으로는 int(a)를 해주면 3 이 될줄 알았는데. 오류가 뜬다. 바꿔줄수 없다고 한다.

그래서 문자열 a를 우선 실수(float)로 바꿔주고 다음 정수로 바꿔줘야 문자열 3.5를 정수로 바꿀수가 있었다.

틀린 예시)

```
a = '3.5'
a = int(a)
>> 에러발생
```

맞는 예시)
```
a = '3.5'

a = float(a)     # 이때 a는 실수형 3.5가 된다.

a = int(a)       

# 이러면 실수형 3.5가 정수형으로 바뀌며 3이 되고 에러가 발생하지 않는다.

print(a)
>>3
```

### **2022-12-15**

#### **쓰면 안되는 변수명들**

False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield