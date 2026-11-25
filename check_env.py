import os, sys, importlib.util
from dotenv import load_dotenv

ok = True
print("python", sys.version.split()[0], "OK" if sys.version_info[:2] == (3, 11) else "-> 3.11 권장")
for pkg in ["openai", "dotenv", "pydantic"]:
    found = importlib.util.find_spec(pkg) is not None
    ok &= found
    print(f"{pkg:<10}", "OK" if found else "없음 (pip install -r requirements.txt)")
load_dotenv()
key = os.getenv("OPENAI_API_KEY", "")
print("OPENAI_API_KEY", "OK" if key.startswith("sk-") else "없음 또는 형식 오류 (.env 확인)")
sys.exit(0 if ok and key else 1)
