# edu-2026h1-dev-setup

2026 상반기 1·2회차 실습 저장소입니다.

- EDU-2026-H1-01 개발환경 세팅과 API 호출 (개정판) (2026-03-05)
- EDU-2026-H1-02 API Key 보안과 환경 변수 관리 (2026-03-12)

환경: Python 3.11, Conda 환경 `hs-2026h1`

```bash
conda create -n hs-2026h1 python=3.11 -y && conda activate hs-2026h1
pip install -r requirements.txt
cp .env.example .env
python check_env.py
```

| 파일 | 회차 | 내용 |
| --- | --- | --- |
| `check_env.py` | 1 | 파이썬 버전, 패키지, 키 설정 점검 |
| `api_call.py` | 1 | API 호출과 usage |
| `structured_output.py` | 1 | JSON 형식으로 받기 |
| `key_safety/scan_secrets.py` | 2 | 커밋 전에 키 패턴 찾기 |
| `key_safety/pre-commit-config.yaml` | 2 | 커밋할 때 자동 검사 |
| `key_safety/INCIDENT.md` | 2 | 키가 유출됐을 때 할 일 |
