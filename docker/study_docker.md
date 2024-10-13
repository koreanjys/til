# Docker 공부 (`from lainyzine.com`)

## **Part.1 docker install**

- windows 11 pro에서는 Hiper-V 기반과 WSL2 기반으로 도커엔진이 사용 가능. 본인은 안정성이 더 좋은 WSL2 채택

### 1.1 윈도우 파워셀 실행(관리자 권한)

### 1.2 명령어 작성
- ```$ wsl --install```
- ```$ wsl --set-default-version 2  # wsl 버전 기본값을 2로 설정```

### 1.3 docker 홈페이지에서 `docker desktop for windows` 다운로드 받고 설치

### 1.4 docker `settings`
- General 설정에서 ’Use the WSL 2 based engine’에 체크가 되어있는지 확인 (되어있지 않다면 체크하고 오른쪽 아래의 Apply & Restart 버튼을 클릭)
- 다음으로 왼쪽 사이드바에서 Resource > WSL Integration 메뉴로 이동합니다. ’Enable Integration with my default WSL distro’에 체크되어있는지 확인 (체크가 되어있지 않을 텐데 체크하고 오른쪽 아래의 Apply & Restart 버튼을 클릭해주면 도커 엔진이 재실행)

### 1.5 설치 확인
- 윈도우 파워셀에서 명령어 작성해보기
```
$ wsl -l -v  # docker-desktop과 docker-desktop-data가 Running 상태인지 확인
```
```
$ docker ps  # 명령어 실행 시 아래와 같이 뜨면 정상 작동 중 (설치 완료)
>>> CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## **Part.2 docker 사용해보기**

### 2.1 docker 명령어 이해

- docker 명령어는 대부분 서브 커맨드로 구성 ()안의 내용은 생략 가능한 옵셔널 값

```
$ docker <SUBCOMMAND> (<OPTIONS>)
```

- docker run 명령어의 형식은 아래와 같다.

```
$ docker run (<OPTIONS>) <IMAGE_NAME> (<COMMAND>)
```

- 명령어 예시

```
$ docker run -it --rm rockylinux:9 bash

# -it는 2개의 옵션. 풀어 쓰면 -i, -t가 됨. 리눅스에서는 한글자 옵션의 경우 -를 붙이고 한꺼번에 지정 가능. 다음으로 --는 여러 글자로 이루어진 옵션을 지정할 때 사용, --rm은 하나의 옵션. 여기까지가 (<OPTIONS>)에 해당하는 부분. 중요! 그 다음으로 오는 rockylinux:9가 <IMAGE_NAME>이 된다. 그럼 자연스럽게 bash는 (<COMMAND>)가 된다.
즉, 앞서 실행한 docker run 명령어는 rockylinux:9 이미지를 사용해서, 이어지는 bash 명령어를 실행하라는 의미.
이 docker run으로 실행한 프로세스를 "컨테이너"라고 함.
```

### 2.2 docker 컨테이너 생애주기

- 생성 -> 실행 -> 종료 -> 삭제

- 1. 생성과 실행은 보통 하나로 묶는다. (run)
- 2. 종료: 일회성 프로그램들은 실행하면, 작업을 마치고 자동으로 종료됨. 하지만 셸은 명시적으로 종료할 때까지(exit) 명령어 입력을 기다리는 특수한 명령어다. 셸 프롬프트에서 exit 명령어를 실행해셔셸을 종료할 수도 있지만, docker stop명령어를 사용해서 컨테이너를 종료시킬 수도 있다. `"docker stop"`으로 종료할 때는 뒤에 컨테이너의 ID나 이름을 지정해준다. (종료가 되었는지 확인하려면 docker ps -a로 확인한다.)
```
$ docker stop container_name
$ docker stop 5dc4959b9ff5  # 컨테이너 ID
$ docker stop 5dc495  # 전부 입력하지 않아도 종료가 가능
$ docker kill 5dc495  # 강제종료는 kill 명령어 사용
```
- 3. 삭제: --rm 옵션은 컨테이너를 종료될 때, 컨테이너를 삭제해준다. --rm옵션을 사용하지 않았다면 직접 종료 후 삭제 명령어를 입력한다.

```
$ docker rm 5dc49

$ docker rm -f 5dc49  # -f 옵션은 컨테이너가 실행중일 때 컨테이너를 강제 종료하고 삭제한다.
```
`종료된 컨테이너를 일괄 삭제하기`
```
$ docker container prune
```

### 2.3 docker 이미지와 docker hub

- 이미지를 처음 시작할 때 로컬에 저장이 되는데, 저장된 이미지 목록을 확인하는 명령어가 있다.

```
$ docker images
$ docker image ls
```
- 위 두 명령어는 같은 명령어다.
- 저장소(Repository)와 태그(Tag)를 :으로 연결해주면 (rockylinux:9) 각각 저장소와 태그 값을 갖는다.
- :로 태그를 붙여주지 않는다면 최신을 의미하는 latest 값으로 자동으로 사용된다.
- 하나의 이미지 저장소에는 다수의 태그가 있다. 저장소가 같더라도 태그가 다르면 전혀 다른 이미지.
- 이 이미지들은 `Docker Hub`에서 찾을 수 있다. 그리고 각 이미지의 설명도 볼 수 있다.
- run 명령어 대신 docker pull image_name(:Tag) 으로 이미지를 받을 수 있다.
- 이미지를 삭제하는 명령어

```
$ docker rmi <image_name:tag>
$ docker image rm <image_name:tag>
# 두 명령어는 같다. 이미지를 삭제하기 전에는, 먼저 해당 이미지를 사용하는 모든 컨테이너를 종료해야 한다.
```

### 2.4 docker로 FFmpeg을 포터블 앱으로 활용하기

- docker는 docker 이미지와 docker hub의 조합으로 아주 높은 이식성을 자랑한다.
- docker의 이식성을 활용하면, docker를 리눅스 포터블 앱으로 활용할 수도 있다. 즉, 시스템에 어떤 프로그램을 설치하지 않고도 리눅스 환경 그대로 프로그램을 실행할 수 있다는 의미.

- Docker Hub 에서 ffmpeg을 검색 <a href="https://hub.docker.com/search?q=ffmpeg" target="_blank">Docker Hub 바로가기</a>
- docker hub에서 가장 좋은건 Docker Official Image를 사용하는것이지만, 없다면 Trusted Content 범주에 있는 것을 받자.
- linuxserver/ffmpeg를 사용해보자.
```
$ docker pull linuxserver/ffmpeg:latest
```

- 예제로 이미지 한 장을 영상 파일로 변환하기
```
# 폴더 생성
## Windows
$ mkdir ~\docker\ffmpeg
$ cd ~\docker\ffmpeg
```

```
# 이미지 파일 다운로드
## Windows
$ wget https://www.lainyzine.com/ko/images/docker-logo.png -OutFile docker-logo.png
```

```
# 이미지 파일 -> 영상 파일 변환
## Windows
$ docker run -it --rm `
  -v ${pwd}:/data `
  linuxserver/ffmpeg:latest `
  -loop 1 -i /data/docker-logo.png -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=320:240 /data/docker-logo.mp4
```
- ffmpeg를 설치하지 않고 도커 이미지만으로 이미지 파일을 영상파일로 변경했다.

### 2.5 도커 볼륨 기능으로 호스트와 컨테이너의 디렉터리 연결하기

위에서 이미지 파일을 영상 파일로 변경하는 코드는 아래와 같다.

```
$ ffmpeg -loop 1 -i docker-logo.png -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=320:240 docker-logo.mp4
```

여기서 ffmpeg 옵션 앞까지 docker 명령어를 다시 한줄로 바꿔보면 다음과 같다.

```
$ docker run -it --rm -v ${pwd}:/data linuxserver/ffmpeg:latest
```

새로 추가된 옵션은 -v 볼륨 옵션이다. Docker 컨테이너는 전용 작업 공간을 가지고 있으며, 기본적으로 호스트의 파일 시스템에 접근할 수 없다. 볼륨 옵션을 사용하면 호스트의 특정 디렉터리를 새로 실행하는 도커 컨테이너 작업 공간의 특정 위치에 마운트해준다.

```
[호스트의 디렉터리]:[컨테이너 내부의 디렉터리]
```
위 예제에서 호스트 디렉터리로, 윈도우에서는 ${pwd}, 맥OS와 리눅스에서는 $(pwd)를 사용한다. 이는 셸에서 사용하는 특수한 구문으로, 괄호 안의 명령어를 실행한 결과값을 대신 입력해준다. 윈도우는 중괄호, 맥과 리눅스에서는 소괄호를 사용한다. 즉, 현재 디렉터리를 전체 경로로 지정한다. 볼륨 옵션에는 상대 경로를 입력할 수 없어서 이 방식을 사용하면 편리하게 작업할 수 있다.

컨테이너 내부의 디렉터리는 /data를 지정했다. 즉, docker 명령어를 실행하는 디렉터리가 Docker 컨테이너 안에서는 /data로 연결된다. 그리고 Docker 컨테이너 안에서 /data에 파일을 생성하면 호스트의 디렉터리에 파일이 추가된다. 볼륨 기능을 통해 컨테이너로 파일을 전달하거나, 작업 결과를 호스트로 편리하게 가져올 수 있다.

최종 명령어는 아래와 같다.
```
## Windows
$ docker run -it --rm `
  -v ${pwd}:/data `
  linuxserver/ffmpeg:latest `
  -loop 1 -i /data/docker-logo.png -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=320:240 /data/docker-logo.mp4

## macOS / Linux
$ docker run -it --rm \
  -v $(pwd):/data \
  linuxserver/ffmpeg:latest \
  -loop 1 -i /data/docker-logo.png -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=320:240 /data/docker-logo.mp4
```

### 2.6 nginx로 알아보는 Docker와 서버 어플리케이션

도커 컨테이너는 독립적인 네트워크 인터페이스를 가지고있다. 그리고 이 네트워크 인터페이스의 특정 포트와 호스트의 특정 포트를 열어서, 컨테이너에서 동작하는 서버 어플리케이션이 외부와 통신하도록 설정할 수 있다. 이 기능이 바로 -p 혹은 --publish 옵션이다. 사용하는 방법은 위에 살펴본 -v 옵션과 비슷하다.

```
$ docker run -d --name nginx-8080 -p 8080:80 nginx

# -p 8080:80
# 앞의 8080은 호스트로 연결할 포트번호.
# 그리고 :(콜론) 문자 뒤의 80은 컨테이너 내부의 포트. 즉, 컨테이너에서 80포트를 지정해서 서버를 실행하면, 호스트의 8080포트로 연결된다.
```

또하나 위에서 -it(커맨드라인에서 프로그램 실행) 대신 -d 옵션을 사용한다. -d 옵션은 컨테이너를 백그라운드에서 실행한다. 이 방식은 주로 서버 어플리케이션을 실행할 때 사용한다. 백그라운드 어플리케이션은 로그 명령어와 잘 어울린다.
```
$ docker logs -n 10 -f <컨테이너 ID>
# -n 10 은 로그를 10줄 표시
# -f 는 실시간으로 로그 확인
# 로그를 종료하려면 CTRL + C 키를 입력
```

### 2.7 Docker로 nginx 서버 여러 대 실행하기

nginx 컨테이너를 하나 더 실행하면..

```
$ docker run -d --name new-nginx-8080 -p 8080:80 nginx
# --name 옵션은 컨테이너에 내가 원하는 이름을 붙여줄 수 있다.

# 실행 시 에러 발생한다.
```
컨테이너는 생성했지만, 호스트의 8080 포트가 이미 사용중이므로, 8080 포트를 사용할 수 없다고 컨테이너를 실행하지 못한다. 그리고 서버 어플리케이션인 nginx를 실행할 때 사용하지 않는 옵션이 있는데, 바로 컨테이너를 삭제하는 --rm 옵션이다.

이 옵션을 사용했다면, 컨테이너가 종료되자마자 삭제되어버린다. 컨테이너가 삭제되면 디버깅을 하거나, 로그를 확인할 수 없다. 이 옵션을 사용하지 않았기 때문에 docker ps -a 명령어로 시작하지 못한 nginx 컨테이너를 확인할 수 있다.
```
$ docker ps -a
# 실행되지 못하고 생성만 된 컨테이너 목록이 출력된다(포트도 없다).
```

이번에는 포트를 바꾸고 실행해본다.
```
$ docker run -d --name nginx-8081 -p 8081:80 nginx
```
이제 웹 브라우저에서 127.0.0.1:8081에 접속해보면, nginx 서버를 확인할 수 있다.

8080 포트에 연결된 nginx 서버 한 대, 그리고 8081 포트에 연결된 nginx 서버가 실행중인 상태이다. 도커를 사용하면 같은 서버 어플리케이션을 여러 번 실행하는 것도 아주 손쉽게 가능하다.


### 2.8 nginx 서버에서 직접 만든 HTML 페이지 서빙하는 방법

nginx는 정적 웹사이트를 서빙하거나, 다른 백엔드 서버의 프론트엔드 서버로 많이 사용된다. 여기서 프론트엔드 서버는, 서버를 구성할 때 제일 앞단에서 트래픽을 받아 전처리를 하거나 적절한 백엔드 서버로 트래픽을 전송하는 서버를 의미한다. 이번 예제에서 직접 만든 HTML 파일을 서빙하겠다.

먼저 새로운 작업 디렉터리를 만들고 이동한다.

```
## Windows
$ mkdir $HOME\docker\nginx\
$ cd $HOME\docker\nginx\

## macOS / Linux
$ mkdir -P ~/docker/nginx/
$ cd ~/docker/nginx/
```

아래 내용을 index.html에 저장한다.
```
<html>
<h1>Welcome to Lainyzine Docker Tutorial</h1>
</html>
```

다음 명령어를 실행해서 8082 포트에서 새로운 nginx를 실행한다.

```
## Windows
$ docker run -d --name nginx-static -p 8082:80 -v ${pwd}:/usr/share/nginx/html:ro nginx

## macOS / Linux
$ docker run -d --name nginx-static -p 8082:80 -v $(pwd):/usr/share/nginx/html:ro nginx
```
-v 옵션은 현재 디렉터리를 컨테이너의 /usr/share/nginx/html 디렉터리에 마운트한다. nginx 이미지의 nginx는 기본적으로 이 디렉터리에 있는 파일을 서빙한다. 마지막에 :ro는, 컨테이너에서 이 디렉터리에서 쓰기를 할 수 없도록 읽기 전용으로 마운트하라는 의미이다.

웹브라우저에서 127.0.0.1:8082를 열어본다. 직접 만든 HTML 파일을 확인할 수 있다.

앞에서 만든 HTML 파일을 수정해본다.
```
<html>
<style>
html {
  font-size: 16px;
}

h1 {
  text-align: center;
  margin: 2rem 1rem;
}
</style>
<h1>Welcome to Lainyzine Docker Tutorial</h1>
</html>
```
웹 브라우저에서 CTRL + R을 입력해 새로고침해본다. 변경된 화면이 나타난다.

![html](https://www.lainyzine.com/ko/article/docker-tutorial/assets/image%2020.png)

여기까지 직접 작성한 HTML 파일을 nginx 이미지로 서빙하는 방법을 알아봤다. 이 디렉터리에 HTML, CSS, JavaScript 파일들을 구성하면 웹사이트를 서빙하는 것도 가능하다.

여기까지 사용한 nginx 예제 서버들을 삭제해준다.

```
$ docker rm -f nginx-static nginx-8080 nginx-8081 new-nginx-8080
```

### 2.9 Tensorflow로 딥러닝 개발환경 맛보기

Tensorflow는 딥러닝에 사용되는 파이썬 라이브러리이다. 파이썬이나 커맨드라인에 익숙하지 않다면 Tensorflow 개발 환경을 구축하는 건 쉽지 않은 일이다. 하지만 Docker를 사용하면, 미리 준비된 Tensorflow 개발 환경에서 Jupyter로 웹에서 파이썬 코드를 바로 실행해볼 수 있다. 다음 명령어를 실행한다.

```
$ docker run -d -p 8888:8888 tensorflow/tensorflow:latest-jupyter
```

다음으로 docker ps 명령어를 컨테이너의 상태를 확인한다.

```
$ docker ps
```
정상적으로 실행되었다면, docker logs를 출력한다. Jupyter 서버에 접속하려면 이 로그에서 토큰을 찾아야한다.

```
$ docker logs <Container ID 일부>
```
로그에서 127.0.0.1:8888로 시작하는 주소를 복사하거나, ?token= 뒤의 값을 복사하고, 127.0.0.1:8888을 호스트의 웹 브라우저에서 열어준다. 토큰을 입력하고 다음으로 넘어간다.

![Tensorflow 이미지로 실행한 Jupyter 서버](https://www.lainyzine.com/ko/article/docker-tutorial/assets/jupyter-token.png)

Tensorflow를 사용할 모든 준비가 끝났다. 예제 파일을 실행해서 Python 코드를 실행해볼 수도 있고, 직접 Tensorflow를 사용하는 코드를 작성해서 실행할 수도 있다.

![Juypter 서버에서 실행한 딥러닝 예제 코드](https://www.lainyzine.com/ko/article/docker-tutorial/assets/image%2022.png)*Juypter 서버에서 실행한 딥러닝 예제 코드*

NVIDIA 그래픽 카드를 사용하는 경우, --gpus=all 옵션을 붙여주고, GPU를 지원하는 태그를 사용한다. WSL2 기반 Docker Desktop을 사용하는 윈도우라면 추가 설정 없이 바로 사용할 수 있다. 리눅스에서는 NVIDIA Container Toolkit을 설치해줘야한다.

```
$ docker run -d --gpus all -p 8888:8888 tensorflow/tensorflow:latest-gpu-jupyter
```

### 2.9 Docker로 MySQL 데이터베이스 서버 맛보기

이번에는 Docker로 MySQL 데이터베이스를 사용해본다. 웹 서버는 웹 브라우저로 접속할 수 있다. MySQL은 웹 서버와 마찬가지로 TCP를 사용하지만 독자적인 형식을 사용한다. 따라서 웹 브라우저로는 사용할 수 없고, 전용 클라이언트를 사용해 접속해야한다.

다음 명령어로 MySQL 서버를 실행한다.

```
## Windows
$ mkdir $HOME\docker\mysql\
$ cd $HOME\docker\mysql
$ docker run --name mysql -p 3306:3306 -v ${pwd}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql-password -d mysql:8.0

## macOS / Linux
$ mkdir -p ~/docker/mysql
$ mkdir ~/docker/mysql
# docker run --name mysql -p 3306:3306 -v $(pwd):/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql-password -d mysql:8.0
```

이제 포트를 열어주는 -p와 볼륨을 연결하는 -v 옵션은 이해했다. 여기서 3306은 MySQL에서 기본으로 사용하는 포트이다.

두 번째로 현재 디렉터리를 컨테이너의 /var/lib/mysql 디렉터리에 마운트했다. 이 디렉터리는 MySQL 서버가 데이터를 저장하는 디렉터리이다. 데이터베이스에 데이터를 기록하더라도 컨테이너를 삭제하면 데이터는 모두 사라진다. 그래서 호스트의 디렉터리와 컨테이너의 데이터 디렉터리를 연결해서, 데이터베이스 변경 사항을 -v 옵션으로 마운트한 호스트 디렉터리에 저장한다. 이러면 컨테이너를 삭제하더라도, 다시 이 디렉터리를 마운트해서 MySQL을 실행하면 이전에 저장했던 데이터에 접근할 수 있다.

새로운 옵션이 하나 있다. 컨테이너를 실행할 때 -e 옵션은 환경변수를 설정해준다. 리눅스 어플리케이션에서는 설정 파일을 자주 사용합니다만, 간단한 설정값은 환경변수로 지정하기도 한다. Docker에서는 매우 일반적으로 사용하는 방식이다. MySQL에서 지원하는 모든 환경변수는 이미지 저장소에서 찾아볼 수 있다.

- [mysql - Official Image | Docker Hub](https://hub.docker.com/_/mysql)

MySQL 이미지에서 MYSQL_ROOT_PASSWORD 환경변수는 root 사용자의 비밀번호를 지정하는 용도로 사용된다.

이제 docker ps로 MySQL 서버를 확인해본다.

```
$ docker ps
```

이제 MySQL 클라이언트를 사용해 데이터베이스에 접속해보겠다. 여기서는 무료로 사용할 수 있는 데이터베이스 클라이언트 DbVisualiser를 사용해보겠다. 먼저 다음 페이지에서 자신이 사용하는 운영체제 버전을 다운로드 받고 인스톨러의 안내에 따라 클라이언트를 설치한다.

- [Download DbVisualizer SQL client - For Windows, macOS, Linux](https://www.dbvis.com/download/)

![DbVisualizer Download](https://www.lainyzine.com/ko/article/docker-tutorial/assets/image%2023.png)*MySQL 클라이언트 DbVisualizer를 다운로드 한다*

처음 실행하면, 라이센스를 등록할지 무료로 사용할지 선택할 수 있다. 여기서는 무료 버전을 선택한다.

![Get Started](https://www.lainyzine.com/ko/article/docker-tutorial/assets/image%2024.png)*무료 모드를 선택*

데이터베이스 연결 버튼을 클릭하고 MySQL 8 버전 커넥터를 선택한다.

![db connect](https://www.lainyzine.com/ko/article/docker-tutorial/assets/dv1.png)*새로운 데이터베이스 접속을 생성*

![db server](https://www.lainyzine.com/ko/article/docker-tutorial/assets/image%2026.png)*접속할 데이터베이스 서버의 정보를 입력*

연결 정보를 입력한다. Name에는 적당한 이름을 붙여준다. Database Userid는 root, Database Password는 Docker를 실행할 때 지정한 mysql-password를 입력한다. Connect 버튼을 클릭하면 데이터베이스 연결된다.

![db query](https://www.lainyzine.com/ko/article/docker-tutorial/assets/dv2.png)*lainyzine 데이터베이스를 하나 생성*

다음으로 1번 아이콘을 클릭해 데이터베이스 쿼리 창을 연다. 2번 에디터에 쿼리를 입력한다.
```
CREATE DATABASE lainyzine
```
3번 쿼리 실행 버튼을 클릭한다. 왼쪽 위의 새로고침 아이콘을 클릭하고, 왼쪽 사이드바에서 lainyzine 데이터베이스가 추가된 것을 확인해본다.

![](https://www.lainyzine.com/ko/article/docker-tutorial/assets/dv3.png)*데이터베이스 접속을 종료한다*

접속을 종료한다.

이제 작업 디렉터리에서 파일 목록을 한 번 출력해본다.

```
$ ls
```
MySQL 데이터베이스를 저장하기 위한 여러 파일들이 생성되어있다. 이제 서버를 종료하고 삭제한다.

```
$ docker stop mysql
$ docker rm mysql
```
여기서부터는 직접 해보자. 먼저 다음 명령어로 작업 디렉터리를 마운트하지 않고 MySQL을 실행한다.
```
$ docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mysql-password -d mysql:8.0
```
그 다음 DbVisualizer에서 접속해서 lainyzine 데이터베이스가 있는지 확인한다.

이 서버를 종료하고 삭제한다. 그리고 다시 작업 디렉터리를 마운트하고 MySQL 서버를 실행한다.
```
$ docker run --name mysql -p 3306:3306 -v ${pwd}:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=new-password -d mysql:8.0
```
그리고 DbVisualizer에서 다시 접속해서 lainyzine 데이터베이스를 확인한다. 위 명령어를 자세히 보면 환경변수가 적용되는지 확인할 수 있도록 패스워드 값도 변경했으니 참고한다.

환경변수로 설정값을 지정하거나, 데이터를 호스트 디렉터리에 저장하는 패턴은 Docker에서는 자주 사용하는 패턴이니, 꼭 직접 실행해보고 익숙해지자.


## **Part.3 Docker 이미지 생성**

### 3.1 docker build

`docker build` 명령어는 `docker image`를 빌드할 때 다음 두가지를 사용한다.

- `Dockerfile`
- `build context`

`Dockerfile`은 텍스트 파일이고, build 시 사용될 명령어들을 모아놓은 것이다.

`build context`는 `PATH`또는 `URL`을 통해 **지정된 다수의 파일을 갖는 경로(위치)**이다.

여기서 말하는 `PATH`는 현재 로컬의 파일 시스템의 디렉터리이고, `URL`은 `Git repository`의 위치이다.

이런 context 경로는 하위의 모든 것들을 재귀적(recursively)으로 build 시에 사용한다.

`docker build`명령어를 아래처럼 사용하면 현재 디렉터리를 `build context`로 지정한 것이다.
```
$ docker build .
# . 은 현재 경로를 의미
```

`docker build`의 실제 처리는 `Docker daemon`이 한다.

`docker build` 요청이 시작되면, 제일 먼저 `Docker daemon`에게 `build context`의 하위 모든 파일에 대한 정보(contents)를 전송한다.

`build context`내에서 원치 않는 build에 사용하지 말았으면, 즉 무시했으면 하는 목록도 존재한다. 그런것은 `.dockerignore`파일에 기재하면 된다.

일반적으로 Dockerfile은 `build context`의 root 경로에 넣는다. 하지만 다른 경로에 있는 Dockerfile을 쓰고 싶다면 아래처럼 한다.

```
$ docker build -f /path/to/a/Dockerfile .
```

`Docker daemon`은 `docker build` 명령어를 수행하는 과정에서 `Dockerfile`을 사용한다. 그리고 안에 기재된 명령어들을 수행한다.

필요하다면 하나의 명령어의 결과에 대해서 새로운 이미지를 중간에 생성한다. 최종적으로 build가 완료되면 최종 완성 이미지의 ID를 출력하고 `Docker daemon`에서 사용된 `build context`의 모든 정보들은 clean up 된다.

`docker build`는 `build cache`라는 것을 사용한다. 기존에 `docker build`를 통해서 생성된 이 캐시는 이후에 build할 때 사용되어 더욱 빠른 빌드 속도를 낸다.


### 3.2 Dockerfile 포맷

