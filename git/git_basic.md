# git 사용법

## ※ WARNING
1. **현재 위치를 잘 확인한다.**
2. **Repo 안에서 repo (master)를 만들지 않는다. (Master 떠있으면 `git init` X)**
3. **Home(`~`)에서 init 하지 않는다.**
4. **(지금은) github에서 직접 수정하지 않는다.**

---
## 프로젝트 초기화 진행

### 계정 세팅

```sh
# (계정당 1회) 서명이 등록되지 않았다면, 계정용 서명 등록
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서@쓸메일주소'
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig  
```

### 프로젝트 생성부터 push까지

```sh
# 프로젝트 폴더 생성
$ mkdir new_project

# 프로젝트 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore

# gitignore.io 에 접속하여 필요한 내용 복-붙

# 폴더를 리포로 초기화
$ git init

# README & .gitignore 파일 add(tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# github에서 원격 저장소 직접 생성

# 생성한 원격 저장소 등록  (origin 은 별명)
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit들 모아서 push
$ git push origin master
```
---

## 명령어 정리

1. 리포 초기화 시점에 1회 입력

```sh
$ git init 
```

2. 작업 후 스테이징

```sh
# 특정 파일만 add 할 때
$ git add <filename>
# 현재 폴더 전체를 add 할 때
$ git add .
```

3. 커밋 진행

```sh
# 메시지는 짧고 정확하게
$ git commit -m 'MESSAGE'
```


4. 모니터링 명령어

```sh
# 현재 Working Dir 과 Stage 상황 확인 (주기적으로 확인하자!)
$ git status

# commit 로그 
$ git log     
# commit 로그 짧게
$ git log --oneline
```

5. github 에 원격 저장소 생성하기 (github site에서 `New Repository`)
  
6. 원격 저장소(remote repo) 추가하기

```sh
$ git remote add origin <URL>
``` 

7. 원격 저장소 확인하기

```sh
$ git remote -v
```

8. 원격 저장소에 지금까지의 commit 들 PUSH 하기

```sh
$ git push origin master
```

9. 새로운 컴퓨터에서 기존 원격 저장소 복제하기
```sh
$ git clone <URL>
```

10. 원격 저장소의 내용 받아오기
```sh
$ git pull origin master
```

|상황|명령어|
|--|--|
|집에서 새로운 프로젝트 시작|`$ mkdir project`|
|프로젝트 폴더로 이동|`$ cd project`|
|리포 초기화|`$ git init`|
|README, .gitignore 생성|`$ touch README.md .gitignore`|
|파일 스테이징|`$ git add .`|
|커밋|`$ git commit -m 'first commit'`|
|원격저장소 생성|github 사이트에서 진행|
|원격 저장소 등록|`$ git remote add origin <URL>`|
|원격 저장소 PUSH|`$ git push origin master`|
|다른 컴퓨터에서 원격저장소 복제|`$ git clone <URL>`|
|작업|`add`, `commit`|
|귀가 직전|`$ git push origin master`|
|집 도착 이후|`$ git pull origin master`|
|작업|`add`, `commit`|
|작업 종료|`$ git push origin master`|
|다른 컴퓨터에서 반복|`$ git pull origin master`|


## **git branch**
branch 는 여러 갈래로 버전을 만들 수 있다.

### **명령어** 
b1 이라는 branch를 생성한다.
```
git branch b1
```
- b1 이라는 branch로 이동한다.(HEAD가 b1을 가리킨다.)
```
git switch b1
```
- master(기존) 로 이동한다. (HEAD가 master를 가리킨다.)
```
git switch master
```
- master 가 b1 위치로 이동한다.
```
(master)
git merge b1
```
- branch b2 생성과 HEAD 가리키는걸 동시에 하는법
```
git switch -c b2
```
- b1 과 b2 가 각자 개발한걸 합치는 방법
```
(b1 or b2)
git merge (b1 or b2)
```
- HEAD 가 현재 가리키는걸 보는 법
```
git branch
```

### **branch 개발방법**

1. HEAD 는 현재 (master) 를 가리키고 있다.
2. branch 를 하나 생성한다.
3. 생성한 branch 로 개발을 차근차근 해 나간다.
4. 완전하게 잘 동작한다면 master 로 merge 한다.

- github 에서 origin(remote) main 혹은 master 가 (master) 라고 보고
나머진 git branch (name) 으로 생성해서 각각 commit

### **단축키 만들기 Alias**

- 명령어를 길게 쓰는게 번거롭다면 `git config`를 이용해 짧게 줄일 수 있다.
```
$ git config --global alias.sw switch
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```
- 위 처럼 설정해 놓으면 `git status`를 `git st`로 짧게 쓸 수 있다.

### **단축키 만들기 윈도우**

- git이 아니고 windows 에서 bash shell 에 단축키 만들려면
- 홈 디렉토리에 `.bash_profile` 을 만들어서 
```
alias gl='git log --oneline --graph'
alias jn='jupyter notebook'
```
위와 같은 내용을 적어 넣으면 된다.

### **Git merge**

1. Fast Forward Merge
   - 가장 기본적인 merge는 바로 Fast Forward Merge이다. 현재 branch 의 HEAD 가 대상 branch 의 HEAD 까지로 옮기는 merge 이다. Fast Forward Merge 는 다음 명령어를 통해 가능하다.

```
$ git switch [branch] => 기존 branch 를 현재 branch로 HEAD를 지정한다.


$ git merge [대상 branch] => 현재 branch 를 대상 branch로 덮어쓴다.
```

이후 작성은 https://kotlinworld.com/277#Fast%--Forward%--Merge 참조

