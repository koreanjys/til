# Git 기초

## Git 의 개념과 학습이유

### VCS
- 버전 컨트롤 스페이스?
### Working directory
- 작업공간
### Stage
- 작업한것을 무대로 올림
### Commit
- 무대위를 사진으로 찍음
## Git 사용법

- 폴더를 생성한다 . 예) mkdir example
- .git 폴더 생성 명령어부터 계정 연결?까지(git init)
``` 
.git 폴더를 생성
$ git init

유저 이메일주소 설정
$ git config --global user.email "example@gmail.com"

유저 네임 설정
$ git config --global user.name "name"

워킹 디렉토리에서 작업한것을 스테이지에 올린다
$ git add 파일

스테이지에 올라온것을 사진찍고 워킹디렉토리로 보낸다.(변경내용을 메모해야한다.)
$ git commit -m '변경내용 메모'

현재 '워킹 디렉토리' '스테이지' '커밋' 관련 상태확인
$ git status

그동안 작업한 이력을 본다.
$ git log
```
