# 2025-02-19
## 클린코드(Clean-Code)
- 이해하기 쉽고 협업하기 쉬운코드
- `유지보수`와 `재사용`이 용이한 코드
- 요구사항을 충실히 잘 반영한 코드 (품질)
- 품질을 확보하면서 개선할 수 있는 코드

## 요구사항과 소프트웨어 아키텍처
- 기능적 요구사항: ID와 PW로 로그인.
- 품질적 제약사항: 1000명이 동시에 로그인을 해도 모두 1초 이내 응답
    - S/W 구조를 이용해서 해결
    - S/W의 구성항목(모듈)과 그들이 상호 연계하는 방식으로 해결
    - S/W 아키텍처, 아키텍처 스타일
- 보안 요구사항: ID와 PW는 중요한 기능이므로, 암호화하고 반복공격에 대비

## 개발 방법론
- 절차, 도구, 산출물, 원칙(원리)
    - 구조적 개발 방법론: 함수를 잘 개발하고 이것을 호출/연계해서 전체 S/W 구축
    - 객체지향 개발 방법론: Class(객체)를 재사용하고 이들을 연계해서 전체 S/W 구축
        - `함수`를 재사용하고 관리하는것보다 `Class`로 재사용하고 관리하면 더 좋다. 장점으로 `변수`를 Class 내부에서 관리할 수 있다. 재사용하기 좋다.
    - 웹서비스 개발 방법론: 웹 표준 기술을 이용해서 기능을 구현하고 연계해서 전체 S/W 구축
    - 결론: 좋은 모듈을 만드는것
        - 좋은 모듈이란 `요구사항을 잘 반영`, `재사용, 유지보수가 용이`, `하나의 책임`, `하나의 목적(기능)`

## 모듈의 품질 척도
### 결합도 (Coupling)
모듈 간의 연결 정도를 의미하며, 결합도가 낮을수록 모듈 간 의존성이 적어 유지보수나 확장에 유리

- **자료 결합도**: 모듈간에 `데이터만` 주고받음 (낮음)
- **스탬프 결합도**: 모듈간에 서로 `자료구조`를 참조하는 형태
- **제어 결합도**: 어떤 모듈이 다른 모듈의 `논리적 흐름을 제어하는 제어요소`를 전달하는 경우
- **외부 결합도**: 다른 외부 모듈의 `데이터를 참조`하는 형태
- **공용 결합도**: 여러 모듈이 하나의 `공통 데이터 영역`을 참조하는 형태. 대표적으로 `전역변수`
- **내용 결합도**: 어떤 모듈이 사용하려면 다른 모듈의 내부 기능과 데이터를 직접 참조해 그대로 가져와 사용하거나 수정하는 경우 (높음)

결합도는 **낮을수록 좋음**

### 응집도 (Cohesion)
모듈 내부에서 관련 있는 데이터와 기능이 모여 있는 정도를 의미하며, 응집도가 높을수록 모듈이 하나의 책임을 잘 수행합니다.

- **기능적 응집도**: 모듈 내 모든 기능이 단일 목적을 위해 수행 (최고)
- **순차적 응집도**: 출력값이 입력값의 결과로 이어짐
- **교환적 응집도**: 동일한 입력과 출력을 사용하여 다른 기능을 수행
- **절차적 응집도**: 관련 기능이 순차적으로 수행됨
- **시간적 응집도**: 특정 시간에 수행해야 할 활동들을 처리
- **논리적 응집도**: 유사한 성격의 처리 요소들이 모여 있음
- **우연적 응집도**: 관련 없는 기능들이 모여 있음 (최저)

응집도는 **높을수록 좋음**.

## 다양한 프로그래밍 언어
- C언어: Low 레벨 언어 -> 메모리 주소에 직접 접근가능
- JAVA: 객체지향, 컴파일
- Python: 객체지향, 인터프리터

## 학습 웹
- 위키독스 ( https://wikidocs.net/ )
- W3Schools Online Web Tutorials  ( https://www.w3schools.com/ )
- 자바스크립트 ( https://ko.javascript.info/ )

## 동기식 비동기식
- 동기식: 작업을 처리하는 동안 다른 작업은 기다린다. 즉, 하나의 작업이 끝난 후에 다음 작업을 시작하는 방식
- 비동기식: 작업을 시작한 후 다른 작업을 동시에 진행할 수 있는 방식

## 자바스크립트
- 다양한 함수 정의 방법
- 비동기식 호출 방법
- 패키지 설치
    - npm -y init 먼저 선언 -> package.json 생성
    - 프로젝트 디렉토리에 설치할때는 npm install {packageName} --save
    - 전역에서 실행 가능한 프로그램 설치 npm install {programName} -g

## 계산기 웹 만들기
- 우선 `npm -y init` -> `npm install express --save` 패키지 설치
- calc.js
    ```
    let express = require("express");
    let fs = require("fs");
    let path = require("path");

    let app = express();
    app.listen(8888);
    console.log("Runnning...");

    app.get("/", (req, res) => {
    res.send("Hello World");
    });

    app.get("/test", (req, res) => {
    var file = path.join(__dirname, "public", "test.html");
    var data = fs.readFileSync(file, "utf-8");
    res.send(data);
    });

    app.use('/calc', express.static(__dirname + '/public'));
    ```
- public/test.html
    ```
    <h1>Hello World</h1>
    ```
- public/index.html
    ```
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Calc</title>
    
        <style>
            table {
                border-collapse: collapse;
            }
            td {
                padding: 5px 10px;
                text-align: center;
            }
            input {
                text-align: right;
                border: none;
            }
            input:focus {
                outline: none;
            }
        </style>
    
    </head>
    <body>
        <table border="1">
            <tr>
                <td colspan="4">
                    <input type="text" id="display">
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <input type="text" id="result">
                </td>
            </tr>
            <tr>
                <td colspan="3" onclick="reset()">AC</td>
                <td onclick="add('/')">/</td>
            </tr>
            <tr>
                <td onclick="add(7)">7</td>
                <td onclick="add(8)">8</td>
                <td onclick="add(9)">9</td>
                <td onclick="add('*')">*</td>
            </tr>
            <tr>
                <td onclick="add(4)">4</td>
                <td onclick="add(5)">5</td>
                <td onclick="add(6)">6</td>
                <td onclick="add('-')">-</td>
            </tr>
            <tr>
                <td onclick="add(1)">1</td>
                <td onclick="add(2)">2</td>
                <td onclick="add(3)">3</td>
                <td onclick="add('+')">+</td>
            </tr>
            <tr>
                <td colspan="2" onclick="add(0)">0</td>
                <td onclick="add('.')">.</td>
                <td onclick="calculate()">=</td>
            </tr>
        </table>
        <script>
            function add(char) {
                var display = document.getElementById('display');
                display.value = display.value + char;
            }
            function calculate() {
                var display = document.getElementById('display');
                var result = eval(display.value);
                document.getElementById('result').value = result;
            }
            function reset() {
                document.getElementById('display').value = "";
                document.getElementById('result').value = "";
            }
        </script>
    </body>
    </html>

    ```
- index.html 태그 정리
    - **`<html>`**: HTML 문서의 시작과 끝을 나타냅니다.
    - **`<head>`**: 문서의 메타데이터, 스타일, 스크립트 등이 들어가는 부분입니다.
    - **`<title>`**: 브라우저 탭에 표시될 문서의 제목을 설정합니다. 여기서는 `"My Calc"`로 설정되어 있습니다.
    - **`<style>`**: HTML 문서 내에서 CSS 스타일을 정의하는 부분입니다.
    - `table`: 테이블의 경계를 밀착시킴 (border-collapse).
    - `td`: 셀에 패딩과 텍스트 정렬 설정.
    - `input`: 텍스트 입력창의 스타일을 설정 (오른쪽 정렬, 테두리 없음, 포커스 시 아웃라인 없애기).
    - **`<body>`**: 문서의 본문 부분입니다. 실제 화면에 표시되는 내용이 이 안에 포함됩니다.
    - **`<table>`**: 계산기의 버튼을 배치하는 표입니다.
    - `border="1"`: 테이블의 경계를 설정합니다.
    - **`<tr>`**: 테이블 행(row)을 정의합니다. 각 계산기 버튼이 이 태그 안에 배치됩니다.
    - **`<td>`**: 테이블의 각 셀(cell)을 정의합니다. 계산기 버튼들이 이 안에 위치합니다.
    - **`<input>`**: 사용자 입력을 받는 텍스트 상자를 정의합니다. 
    - `id="display"`: 계산기에서 입력을 보여주는 화면.
    - `id="result"`: 계산 결과를 표시하는 화면.
    - **`colspan="4"`**: 셀을 4개의 열을 가로지르도록 병합합니다. 주로 디스플레이 영역이나 버튼 레이아웃에 사용됩니다.
    - **`onclick`**: 버튼 클릭 시 실행할 자바스크립트 함수입니다. 각 버튼에 대한 클릭 이벤트가 정의되어 있습니다.
    - 예: `onclick="add(7)"`은 숫자 `7`을 `display`에 추가하는 함수입니다.
- 자바스크립트 함수 정리
    - **`add(char)`**: 숫자나 연산자를 `display` 텍스트박스에 추가합니다.
    - **`calculate()`**: `display`의 수식을 계산하고, 그 결과를 `result` 텍스트박스에 표시합니다.
    - **`reset()`**: `display`와 `result` 텍스트박스를 초기화합니다 (빈 문자열로 설정).
