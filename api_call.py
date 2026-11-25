from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(timeout=20, max_retries=2)
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "헤이트슬롭 사내 교육 도우미다."},
              {"role": "user", "content": "가상환경을 쓰는 이유를 한 문장으로."}],
)
print(r.choices[0].message.content)
print(r.usage)
