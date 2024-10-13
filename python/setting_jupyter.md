## 가상환경(venv)에서 jupyter notebook 실행 및 연결 하려면..
1. 가상환경을 생성한다.
```
$ python -m venv venv
```
2. 가상환경에 연결
```
$ source venv/Script/activate
```
3. jupyter 설치
```
(venv)$ pip install jupyter
```
4. ipykernel 설치
```
(venv)$ pip install ipykernel
```
5. jupyter에 커널 추가(myenv는 유동적으로 변경해줄 수 있다.)
```
(venv)$ python -m ipykernel install --user --name=myenv
```