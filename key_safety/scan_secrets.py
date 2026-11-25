# 사용법: python key_safety/scan_secrets.py [경로]
import re, sys
from pathlib import Path

PATTERNS = {"OpenAI": re.compile(r"sk-[A-Za-z0-9_-]{20,}"), "HF": re.compile(r"hf_[A-Za-z0-9]{30,}")}
SKIP = {".git", ".venv", "__pycache__"}
found = 0
for p in Path(sys.argv[1] if len(sys.argv) > 1 else ".").rglob("*"):
    if p.is_dir() or SKIP & set(p.parts) or p.name == ".env":
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for name, pat in PATTERNS.items():
        for m in pat.finditer(text):
            found += 1
            print(f"[{name}] {p}: {m.group()[:8]}...")
sys.exit(1 if found else 0)
