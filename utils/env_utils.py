import os
from dotenv import load_dotenv

load_dotenv(override=True)

# api
DEEPSEEK_API_KEY=os.getenv("DEEPSEEK_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
BAILIAN_API_KEY=os.getenv("BAILIAN_API_KEY")
XIAOAI_API_KEY=os.getenv("XIAOAI_API_KEY")

#url
DEEPSEEK_BASE_URL=os.getenv("DEEPSEEK_BASE_URL")
OPENAI_BASE_URL=os.getenv("OPENAI_BASE_URL")
BAILIAN_BASE_URL=os.getenv("BAILIAN_BASE_URL")
XIAOAI_BASE_URL=os.getenv("XIAOAI_BASE_URL")

TAVILY_KEY = os.getenv("TAVILY_KEY")