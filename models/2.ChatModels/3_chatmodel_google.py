from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI("gemini-1.5-pro")

result = model.invoke('who are the founders of google')

print(result.content)