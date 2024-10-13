# 리눅스 도커와 DB 연결 과정

- 시행착오 끝에 연결함.

1. 리눅스 방화벽에 mysql 포트를 추가해야 되었다. 이유는 디테일하게 모르지만, 외부에서 호스트 mysql에 접근하려면 방화벽에 mysql 포트를 등록해야 했다.
2. 백엔드 소스코드의 engine_url에 "127.0.0.1:3306" 이 부분을 "host.docker.internal"로 바꿔야했다.
3. docker run 할때 옵션 하나를 추가해야 했다.
```
# 이런 식으로 했다. -p 옵션도 줘야함. -d 옵션도 필요해보임.

$ sudo docker run --add-host=host.docker.internal:host-gateway -it 0f922a python main.py

```

겨우 연결됨.
