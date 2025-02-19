# Class

## 객체(Object)와 인스턴스(Instance)

- 객체와 인스턴스는 비슷하지만 약간의 차이가 있다.
- **객체(Object)**: 클래스에 의해 생성된 모든 것을 객체라고 한다.
- **인스턴스(Instance)**: 특정 클래스에서 만들어진 객체를 인스턴스라고 한다. 즉, 객체는 일반적인 개념이고, 특정 클래스에서 생성된 객체를 그 클래스의 인스턴스라고 한다.

```python
class Car:
    pass

my_car = Car()
```
- 위 코드에서 `my_car`는 `Car` 클래스의 **인스턴스**이다. 동시에 `my_car`는 **객체**이기도 하다.

## `self` 키워드

- `self`는 클래스의 인스턴스를 가리키는 특별한 변수이다.
- 클래스 내부에서 정의된 메서드는 기본적으로 첫 번째 인자로 `self`를 받으며, 이를 통해 각 인스턴스별 속성에 접근할 수 있다.

```python
class Car:
    def __init__(self, color):
        self.color = color  # 인스턴스 변수

    def show_color(self):
        print(f"This car is {self.color}.")

car1 = Car("red")
car2 = Car("blue")

car1.show_color()  # 출력: This car is red.
car2.show_color()  # 출력: This car is blue.
```

## `__init__` 메서드

- `__init__`은 클래스의 **생성자(Constructor)**로, 객체가 생성될 때 자동으로 실행된다.
- 인스턴스 변수를 초기화하는 역할을 한다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.introduce()  # 출력: Hi, my name is Alice and I am 25 years old.
p2.introduce()  # 출력: Hi, my name is Bob and I am 30 years old.
```

## 클래스 변수와 인스턴스 변수

- **클래스 변수(Class Variable)**: 클래스 전체에서 공유되는 변수이다.
- **인스턴스 변수(Instance Variable)**: 특정 인스턴스에서만 사용되는 변수이다.

```python
class Example:
    class_var = "I am a class variable"

    def __init__(self, value):
        self.instance_var = value  # 인스턴스 변수

obj1 = Example("I am instance 1")
obj2 = Example("I am instance 2")

print(obj1.class_var)  # 출력: I am a class variable
print(obj2.class_var)  # 출력: I am a class variable

print(obj1.instance_var)  # 출력: I am instance 1
print(obj2.instance_var)  # 출력: I am instance 2

Example.class_var = "Class variable changed!"
print(obj1.class_var)  # 출력: Class variable changed!
print(obj2.class_var)  # 출력: Class variable changed!
```

## 클래스 내부 변수 (클래스 전역 변수)

- 클래스 내부에서 `def` 없이 바로 선언한 변수는 클래스 변수(전역 변수)가 된다.
- 모든 인스턴스가 해당 변수를 공유한다.

```python
class Hi:
    greeting = 'hi'  # 클래스 변수

obj1 = Hi()
obj2 = Hi()

obj1.greeting = 'hello'  # obj1의 인스턴스 변수로 변경
print(obj1.greeting)  # 출력: hello
print(obj2.greeting)  # 출력: hi
print(Hi.greeting)  # 출력: hi
```

- `obj1.greeting`을 변경했지만, 이는 `obj1`의 인스턴스 변수로 새롭게 설정된 것이며, `obj2`와 `Hi` 클래스의 `greeting`에는 영향을 주지 않는다.

## 정리

| 개념 | 설명 |
|---|---|
| **객체(Object)** | 클래스로부터 생성된 모든 것 |
| **인스턴스(Instance)** | 특정 클래스에서 생성된 객체 |
| **self** | 클래스 내부에서 인스턴스를 참조하는 변수 |
| **`__init__`** | 객체가 생성될 때 자동으로 실행되는 생성자 메서드 |
| **클래스 변수** | 클래스 전체에서 공유되는 변수 |
| **인스턴스 변수** | 특정 인스턴스에서만 사용되는 변수 |

이와 같이 클래스를 활용하면 코드의 재사용성을 높이고, 구조적인 프로그래밍이 가능해진다.