from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    key_themes : Annotated[list[str],'Write down all the key points in a list']
    summary : Annotated[str,"A brief description of the review"]
    sentiment: Annotated[str,'Return sentiment of the review either negative,positive or neutral']
    pros:Annotated[Optional[list[str]],'Write down all the pros in a list']
    cons:Annotated[Optional[list[str]],'Write down all the cons in a list']

Structured_model = model.with_structured_output(Review)

result = Structured_model.invoke("""The hardware is great,but the software feels bloated. There are too many pre-installed apps that i can"t remove.Also, the UI looks outdated compared to other brands. Hoping for a software update to fix it
    """
)

print(result)
print(result['summary'])
print(result['sentiment'])