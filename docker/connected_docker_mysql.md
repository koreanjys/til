### 리눅스에서 Docker 서비스와 MySQL(DB) 연결 과정
시행착오 끝에 연결 성공!

#### **1. 리눅스 방화벽에서 MySQL 포트(3306) 열기**  
- MySQL 서버가 외부에서 접근 가능하려면 방화벽에서 3306 포트를 열어야 합니다.  
- 리눅스 방화벽(UFW, iptables 등)에 따라 설정 방법이 다를 수 있음.  

  **예제(UFW 사용 시)**
  ```sh
  $ sudo ufw allow 3306/tcp
  $ sudo ufw reload
  ```

#### **2. 백엔드 소스코드 수정**
- MySQL을 Docker 컨테이너 내부에서 접근하려면 `127.0.0.1` 대신 `host.docker.internal`을 사용해야 합니다.
- **수정 전**
  ```python
  engine_url = "mysql://user:password@127.0.0.1:3306/dbname"
  ```
- **수정 후**
  ```python
  engine_url = "mysql://user:password@host.docker.internal:3306/dbname"
  ```

#### **3. Docker 컨테이너 실행 시 `--add-host` 옵션 추가**
- Docker에서 `host.docker.internal`을 사용하려면 `--add-host=host.docker.internal:host-gateway` 옵션을 추가해야 함.
- `-p 3306:3306` 옵션도 필요할 수 있음(MySQL 컨테이너를 외부에서 접근 가능하게 하기 위해).  

**실행 예제**
```sh
$ sudo docker run --add-host=host.docker.internal:host-gateway -p 3306:3306 -d 0f922a python main.py
```
- `--add-host=host.docker.internal:host-gateway` → Docker 컨테이너에서 호스트를 인식하도록 설정  
- `-p 3306:3306` → MySQL 포트 매핑(필요한 경우)  
- `-d` → 백그라운드 실행  

---

### 보완할 점
1. **방화벽 설정이 필요한 이유**  
   - 기본적으로 리눅스 방화벽(UFW, iptables)은 외부에서 MySQL(3306)로 접근하는 것을 막음.  
   - 따라서 **방화벽에서 3306 포트를 열어야 외부 접근 가능**.  
   - 단, 보안상 `bind-address` 설정도 확인 필요(기본적으로 `127.0.0.1`로 제한되어 있음).  

2. **MySQL `bind-address` 설정 확인**
   - `/etc/mysql/my.cnf` 또는 `/etc/mysql/mysql.conf.d/mysqld.cnf` 파일 수정  
   ```sh
   bind-address = 0.0.0.0
   ```
   - `bind-address = 127.0.0.1`이면 외부 접근 불가 → `0.0.0.0`으로 변경 후 MySQL 재시작 필요  
   ```sh
   $ sudo systemctl restart mysql
   ```

3. **Docker 네트워크 사용 고려**
   - `host.docker.internal`이 필요 없는 경우도 있음.  
   - Docker `--network=host` 옵션을 주면 `localhost`로도 연결 가능.  

---

### 최종 정리 (Docker에서 MySQL 연결 과정)
1. **리눅스 방화벽에서 3306 포트 열기**
   ```sh
   $ sudo ufw allow 3306/tcp
   $ sudo ufw reload
   ```
2. **MySQL `bind-address` 설정 변경 (`0.0.0.0`)**
3. **백엔드 코드에서 `host.docker.internal` 사용**
4. **Docker 컨테이너 실행 시 `--add-host` 옵션 추가**
   ```sh
   $ sudo docker run --add-host=host.docker.internal:host-gateway -p 3306:3306 -d 0f922a python main.py
   ```

---

이제 Docker 컨테이너에서 MySQL에 정상적으로 연결