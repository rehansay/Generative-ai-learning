import os

from dotenv import load_dotenv
load_dotenv(".env")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)


class Movie(BaseModel):
    title:str
    release_year:Optional[int]
    genre:List[str]
    director:Optional[str]
    cast:List[str]
    rating:Optional[float]
    summary:str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system',"""
Extract movie information from the paragraph
     {format_instructions}
"""),
("human","{paragraph}")
]
)

para=input("Give your paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions()
     }
)

response=model.invoke(final_prompt)

movie_data = parser.parse(response.content)


print(response.content[0]["text"])
