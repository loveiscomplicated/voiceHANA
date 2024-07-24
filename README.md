# 음성 인식 및 TTS를 사용한 GPT-4 챗봇

이 프로젝트는 음성 인식을 통해 사용자의 입력을 받고, GPT-4 API를 사용하여 응답을 생성하며, TTS를 통해 응답을 음성으로 출력하는 챗봇입니다.

## 설치 및 실행 방법

Python 3.8.19 버전 사용중

### 필요 라이브러리 설치

```bash
pip install -r requirements.txt
```

가상 환경을 구성해서 설치하는 것을 추천드립니다

### Conda를 사용한 가상환경 구성

1. **Conda 설치**: Anaconda 또는 Miniconda를 설치합니다. [Anaconda](https://www.anaconda.com/products/individual) 또는 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)에서 다운로드할 수 있습니다.

2. **가상환경 생성**:
    ```bash
    conda create --name myenv python=3.8
    ```
    여기서 `myenv`는 가상환경의 이름이며, `python=3.8`은 사용할 Python 버전을 의미합니다.

3. **가상환경 활성화**:
    ```bash
    conda activate myenv
    ```

4. **필요한 라이브러리 설치**:
    `requirements.txt` 파일이 있는 디렉토리로 이동한 후 다음 명령어를 실행합니다.
    ```bash
    pip install -r requirements.txt
    ```

5. **가상환경 비활성화**:
    작업을 마친 후 가상환경을 비활성화합니다.
    ```bash
    conda deactivate
    ```


이 단계를 따라가면 가상환경을 쉽게 구성하고 관리할 수 있습니다.



### 마지막으로 main.py 파일을 시행시키면 됩니다
단 처음 실행하기 이전 gpt api 카를 넣어야 합니다

OpenAI API 키 설정
openai.api_key = 'API키를 여기에 넣어주세요@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

API키를 여기에 넣어주세요@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 이 부분을 지우고 API 키를 넣어주세요

## 미래 개선 사항
1. TTS 기술 향상
2. 프롬프트 파일을 따로 만들어 main.py의 간결성 유지
3. 프롬프트 구체화

