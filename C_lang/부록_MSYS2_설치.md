# MSYS2
윈도우에서 MinGW를 설치하여 C/C++ 개발 환경을 구축하는 방법을 단계별로 안내해 드리겠습니다. MinGW는 GCC 컴파일러를 윈도우에서 사용할 수 있도록 해주는 도구입니다.

**1. MSYS2 설치**

MSYS2는 MinGW-w64 도구 체인을 제공하는 플랫폼으로, 최신 GCC 버전과 다양한 개발 도구를 제공합니다.

- **설치 파일 다운로드**: [MSYS2 공식 웹사이트](https://www.msys2.org/)에서 설치 프로그램을 다운로드합니다.
- **설치 실행**: 다운로드한 설치 프로그램을 실행하고, 설치 위치를 선택한 후 설치를 완료합니다.
- **MSYS2 업데이트**: 설치 후 MSYS2 터미널을 열고, 다음 명령어를 입력하여 패키지 데이터베이스와 기본 패키지를 업데이트합니다

  
```bash
  pacman -Syu
  ```

  업데이트 후 MSYS2를 재시작하여 변경 사항을 적용합니다.

**2. MinGW-w64 도구 체인 설치**

MSYS2를 통해 MinGW-w64 도구 체인을 설치합니다.

- **터미널 열기**: MSYS2 터미널을 엽니다.
- **도구 체인 설치**: 다음 명령어를 입력하여 MinGW-w64 도구 체인을 설치합니다

  
```bash
  pacman -S --needed base-devel mingw-w64-x86_64-toolchain
  ```

  설치 중에 필요한 패키지를 묻는 창이 나타나면 기본값을 선택하여 진행합니다.

**3. 환경 변수 설정**

설치한 MinGW-w64의 `bin` 디렉토리를 시스템의 PATH 환경 변수에 추가하여 어디서든 컴파일러를 사용할 수 있도록 설정합니다.

- **환경 변수 편집**:
  - 윈도우 검색 창에 '환경 변수'를 입력하고 '시스템 환경 변수 편집'을 선택합니다.
  - '환경 변수(N)...' 버튼을 클릭합니다.
  - '시스템 변수' 섹션에서 'Path'를 선택하고 '편집'을 클릭합니다.
  - '새로 만들기'를 클릭하고 MinGW-w64의 `bin` 디렉토리 경로를 입력합니다. 기본 설치 경로는 `C:\msys64\mingw64\bin`입니다.
  - 모든 창에서 '확인'을 눌러 변경 사항을 저장합니다.

**4. 설치 확인**

명령 프롬프트를 열고 다음 명령어를 입력하여 설치가 제대로 되었는지 확인합니다


```bash
gcc --version
g++ --version
gdb --version
```

각 명령어를 입력했을 때 버전 정보가 표시되면 설치가 성공적으로 완료된 것입니다.

**참고 사항**

- MSYS2는 64비트 윈도우 8.1 이상에서 지원됩니다.
- 32비트 버전의 MinGW가 필요하다면, MSYS2의 설치 시 32비트 버전을 선택하거나 별도로 설치할 수 있습니다.