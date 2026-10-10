# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()
# model = ChatGroq(
#     model="openai/gpt-oss-20b"
# )

# response=model.invoke("what is cricket?")

# print(response.content)

# from dotenv import load_dotenv


# from langchain.chat_models import init_chat_model

# load_dotenv()
# model = init_chat_model("google_genai:gemini-3.7-flash")

# response=model.invoke("give me a paragraph on Geopolitics")

# print(response.content[0]["text"])




from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.9)

response=model.invoke("Write a poem on introverts")

print(response.content) 


# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI 
 
# load_dotenv()
# model = ChatMistralAI(model="mistral-small-2603")

# response=model.invoke("give me a paragraph on Comparative Religion studies")

# print(response.content) 