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
### **2022-12-19 `Mon`**

#### **함수**

1. 함수 선언할 때, 맞춤법
```
def 함수(a = 10):
    return a * 2
```
위에서 함수 매개변수(a = 10) 에 보면
a 값을 주는것은 기본값을 주는것과 같다.
함수() 이렇게 ()안에 값을 안주면 a = 10으로 기본값을 준다.

근데 저것은 보기 좋은게 아니다. 
함수() 기본값을 줄때 = 사이에 띄어쓰지않는다.

```
def 함수(a=10):
    return a * 2
```
위 처럼 쓴다.

2. def 함수(*t):

매개변수 여러개를 제한없이 받고싶으면 `*(매개변수)`
를 쓴다.

그러면 `*(매개변수)`값이 튜플로 저장이 된다.

3. def 함수(**d):

이렇게 ** 를 붙여서 선언하면 위에 서술한 *는 튜플이 되지만 **는 딕셔너리가 된다.
그래서 `def 함수(a=10, b=11):`
이렇게 선언을 하게되면 매개변수값이 `{'a': 10, 'b': 11}`이렇게 된다~!!

4. def 함수(매개변수1, 매개변수2, 매개변수3 = 'a'):

위에 함수를 선언하면 매개변수1~2는 정의를 해야되고

매개변수3은 정의를 하지 않아도 기본값 'a'를 쓰게 된다.

그런데 만약

```
def 함수(매개변수1 = 'a', 매개변수2, 매개변수3):
    pass
```
위 처럼 선언을 하게된다면 에러메세지가 뜨면서 안된다. 값이 정해진 함수 뒤에 값이 정해지지 않은 함수는 올수없다며..

그러므로

```
def 함수(매개변수1, 매개변수2='b'):
    pass
```
위와같이 `=`이 붙은, 한마디로 기본값이 정의된 함수는 끝에 와야한다. 라고 기억하자.

### **2022-12-20**
#### **함수의 LEGB Rule**
- 여기서 LEGB는 Local < Enclosed < Global < Built-in 을 말한다.


```
# list의 경우 deepcopy와 shallowcopy가 있는데..
# 깊은 카피와 얕은 카피임

a = [1, 2, 3]

def loc():
    b = a
    b.append(4)

# 이렇게 함수를 정의하고 함수를 불러낸다면..?

loc()
print(a)
# >> [1, 2, 3, 4]
# list a의 원소값이 하나 늘어났다.. 이말은 즉슨 referance(리스트, 튜플, 딕셔너리, 집합 등) 중에 변화를 줄수있는것 (list, set 등)은
# Local 안에서도 Global에 있는 값을 변화시킬 수 있다는 것!

# 그래서 만약 1차원만 copy 를 뜨고 싶으면

def loc2():
      # (*주의 : 얕은복사는 1차원 배열만 복사한다. 2차원까지 있는 리스트면 1차원은 복사되고 2차원은 똑같은 값을 가리킨다.)
    b = a[:]
    b.append(5)

loc2()
print(a)
# >> [1, 2, 3, 4]

# 2차원 배열에 적용해보자
a = [[1, 2], [3, 4]]

def loc3():
    b = a[:]
    b.append(0)

loc3()
print(a)
# >> [[1, 2], [3, 4]]    이와같이 잘 복사가 되어 영향을 받지 않았다. 하지만.. 2차원을 건드리면..?

def loc4():
    b = a[:]
    b[0].append(0)

loc4()
print(a)
# >> [[1, 2, 0], [3, 4]]   이와같이 2차원은 수정이 되어버린다.. 고로 2차원 이상을 온전히 복사하려면

import copy  # copy함수를 가져와서

b = copy.deepcopy(a)
b[1].append(0)
print(a)
# >> [[1, 2, 0], [3, 4]]   이렇게 2차원도 수정이 되지 않는다!
```

#### **재귀함수**
- 재귀함수는 매우 계산량이 많아서 느리다.
- 재귀함수는 최대 1000번 깊이까지 있다.

#### **lambda 함수**
```
# 아래와 같이 간단한 함수를 정의해서 사용하는 것이 아니라 간결하게 사용 가능합니다.

l = lambda x, y:x + y

l(1, 2)
>> 3


# 위 lambda 와 밑에 func는 같다.


def func(x, y):
    return x + y

f = func(1, 2)
>> 3
```

### **2022-12-21**

#### **함수 map 과 filter**

map 예시
```
map(function, iterable)

map(int, ['1', '2', '3])
```

map은 iterable의 요소를 function해주고 그 결과값을

주소로 돌려준다.

filter 예시
```
filter(function, iterable)

filter(lambda x: x > 0, iterable)

```
filter는 iterable요소를 function(return 값이 True 나 False)으로 걸러서 True 값만 주소로 돌려준다.

#### **LIST**
리스트는 요소 변경이 가능하다.
그래서 append 나 extend 같은 리스트 함수는
사용했을때 리턴값이 없고, 즉각적으로 변화를 준다.

예시
```
a = [1, 2, 3]
a.append(4)
```
위와같은 경우에 리스트 a는 [1, 2, 3, 4]로 값이

추가되어있다. 그리고  return 값이 없기 때문에

b = a.append(4) 를 해도 변수 b는 None이 된다.

extend 또한 마찬가지.

리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있습니다.

extend 예시를 보자

```
a = [1, 2, 3]
a.extend([4, 5])
```
위와 같이 하면 a에는 [4, 5]가 추가되어

a = [1, 2, 3, 4, 5] 가 된다.

b = a.extend([4, 5]) 이것 역시 return 값이 없기

때문에 b = None 과 같다.

그리고 extend의 특징이 또 있는데

항상 iterable 값이 들어가기 때문에

문자열 'abcd' 이 'a','b','c','d' 로 되어 추가된다.

예시를 보자

```
a = ['a','b','c','d']
a.extend('efg')
print(a)
>> ['a','b','c','d', 'e', 'f', 'g']
```
위와같이 되므로 , 'efg'가 추가하고 싶다면

['efg'] 이렇게 감싸주도록 하자

#### **sort 와 sorted**
- sorted(iterable)

특징은 return 값이 있다. 원본 변수가 변하지 않는다.

list 뿐만 아니라 다른데에도 쓸수있다.

return값은 항상 list다.

```
nums = [3, 5, 2, None, 1, 4]
sorted(nums)
>> Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   TypeError: '<' not supported between instances of 'NoneType' and 'int'

>>> sorted([num for num in nums if num])
[1, 2, 3, 4, 5]
```
위와같이 서로 비교할수있는 값이 들어있어야 한다.

그렇지 않으면 에러가 뜬다.

sorted(iterable, key=function) 이렇게

key값으로 설정을 할수도 있다.

```
>>> countries = [
  {'code': 'KR', 'name': 'Korea'},
  {'code': 'CA', 'name': 'Canada'},
  {'code': 'US', 'name': 'United States'},
  {'code': 'GB', 'name': 'United Kingdom'},
  {'code': 'CN', 'name': 'China'}
]
```
```
>>> sorted(countries)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'dict' and 'dict'
정렬 기준을 설정하려면 sorted() 함수의 key 옵션을 사용해야하는데요. key 옵션에 함수를 지정하면 각 원소에 이 함수를 호출한 결과를 기준으로 대소비교를 하게됩니다.

예를 들어, 국가 코드를 기준으로 정렬을 해볼까요? 이 기준으로 영국(GB)이 한국(KR) 앞에 오게 되네요.

>>> sorted(countries, key=lambda country: country["code"])
[{'code': 'CA', 'name': 'Canada'}, {'code': 'CN', 'name': 'China'}, {'code': 'GB', 'name': 'United Kingdom'}, {'code': 'KR', 'name': 'Korea'}, {'code': 'US', 'name': 'United States'}]
```


- [list].sort()

특징은 return값이 없고, 원본 변수가 즉각적으로 변한다.

list에서만 쓴다.

정렬 설정을 reverse=True 나 key=function 으로

설정할수있다.

예시

```
a = ['a5', 'c3', 'e1', 'b4', 'd2']
a.sort(key=lambda x:x[1])
print(a)
>> ['e1', 'd2', 'c3', 'b4', 'a5']
```
이렇게도 되고
```
data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

#중복 제거
data_list = list(set(data_list))

data_list.sort()
data_list.sort(key=lambda x : len(x))

print(data_list)
```
위처럼 길이별로도 된다.

lambda x: len(x) 의 경우 len(x)를 하면 길이가

2, 3, 5, 9 이런식으로 숫자로 반환되기때문에

그 숫자가 작은 순서대로 정렬을 할것이다.

```
data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

for index in range(len(data_list)) : 
    data_len = len(data_list[index])
    data_list[index] = (data_list[index], data_len)

data_list.sort(key = lambda x :(x[1], x[0]))
print(data_list)
```
위처럼 key=lambda x: (x[1], len(x)) 처럼

(,)로 두가지 경우로 설정해서 정렬할수도 있다.


#### **dictionary**

- dictionary.setdefault(key, value)

setdefault함수를 쓰면, key값이 없어도 value를 반환하고

새로 추가가 된다.

예를 보자

```
dic = {'a': 'apple', 'b': 'banana'}
dic.setdefault('c', 'cat')
>> cat
print(dic)
>>{'a': 'apple', 'b': 'banana', 'c': 'cat'}
```

### **2022-12-22**

#### **Class**

- 관습

함수, 변수 등은 모두 소문자로, 띄어쓰기는 _ 로  ->  snake_case

클래스는 첫글자는 대문자로, 띄어쓰기도 대문자로 -> PascalCase

#### **\__(name)__**

- 인스턴스
- 클래스

위 두가지는..

- 모든 \__*__ 는 type class 상속

#### **module**

```
__name__  은 파일이름

__main__ 은 현재 본인 이름?

```
### **2022-12-23**

#### **request**

우선 pip install requests 를 해야한다.

```
# 뭐가 됐든 client 프로그램을(requests보낼수있는) 준비해서
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1046'

# url을 통해 요청을 한다.(달라고한다)
data = requests.get(url).json()

for no in range(1036, 1047):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={no}'
    data = requests.get(url).json()
    print(data['totSellamnt'])
```
```
import requests

key = '8cb1b55c87ce758e9389d6b2a2d7b92c'
url = 'https://api.themoviedb.org/3/movie/upcomming?api_key=8cb1b55c87ce758e9389d6b2a2d7b92c&language=ko-KR'

data = requests.get(url).json()
-------------------------------------------------
https://api.themoviedb.org/3
/movie                           # 달라질 수 있음
/latest
?
api_key=8cb1b55c87ce758e9389d6b2a2d7b92c
&
language=ko-KR
--------------------------------------------------
```

### **2022-12-26**

#### **코드작성 규칙**

1. list => 복수형 (숫자는 nums or numbers | 문자는 chars or words)
2. 함수 => 동사(함축형) | return 값이 T/F => is_xxx()
3. 변수 => 담긴값이 T/F => is_xxx

#### **코딩할때 설계먼저**

1. 펜과 종이를 준비한다.
2. 문제를 축소해본다.
3. 그림으로 그려가며 알고리즘을 생각해본다.
4. 생각과 필기 혹은 그림이 정리가 되면 문제를 대입해본다. 혹은 코딩을 짠다.
