from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel , Field
load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):

    key_themes: list[str] = Field(description='Write down all the key themes discussed in the review in a list') 
    summary: str = Field(description="A brief description of the review")
    sentiment: Literal['neg','neu','pos'] = Field(description="Return sentiment of the review either negative,positive or neutral'")
    pros: Optional[list[str]] = Field(description='Write down all the pros in a list')
    cons: Optional[list[str]] = Field(description="Write down all the cons in a list")
                        

Structured_model = model.with_structured_output(Review)

result = Structured_model.invoke("""The hardware is great,but the software feels bloated. There are too many pre-installed apps that i can"t remove.Also, the UI looks outdated compared to other brands. Hoping for a software update to fix it
    """
)

print(result)
print(result['summary'])
print(result['sentiment'])