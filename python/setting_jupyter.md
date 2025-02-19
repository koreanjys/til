## Jupyter 노트북을 가상환경 커널에서 실행하는 방법
1. **가상환경 생성**
   ```sh
   $ python -m venv venv
   ```

2. **가상환경 활성화**
   - Windows (CMD/PowerShell)
    ```sh
    venv\Scripts\activate
    ```
   - macOS/Linux
    ```sh
    source venv/bin/activate
    ```

3. **Jupyter 설치**
   ```sh
   (venv)$ pip install jupyter
   ```

4. **IPython Kernel 설치**
   ```sh
   (venv)$ pip install ipykernel
   ```

5. **Jupyter에 가상환경 커널 추가**
   ```sh
   (venv)$ python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
   ```

6. **Jupyter Notebook 실행**
   ```sh
   (venv)$ jupyter notebook
   ```

7. **Jupyter에서 가상환경 선택**
   - 실행 후 **Kernel > Change Kernel**에서 `Python (myenv)` 선택