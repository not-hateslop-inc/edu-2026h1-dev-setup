from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
client = OpenAI()

class Notice(BaseModel):
    title: str
    summary: list[str]
    department: str

text = "다음 주 목요일 정기 교육은 RAG를 다룹니다. 노트북을 지참하세요. 문의는 교육·지식관리부로."
r = client.beta.chat.completions.parse(
    model="gpt-4o-mini", response_format=Notice,
    messages=[{"role": "user", "content": f"공지를 제목, 3줄 요약, 담당 부서로 정리: {text}"}],
)
print(r.choices[0].message.parsed)
