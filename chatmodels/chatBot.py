# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI 
 
# load_dotenv()
# model = ChatMistralAI(model="mistral-small-2603")


# prompt=input("You:")
# response=model.invoke(prompt)

# print(response.content) 

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

messages=[

]
print("_ _ _ _ _ _ _ _ _ welcome type 0 to exit the application _ _ _ _ _ _ _ _ _")

while True:
    
    prompt = input("You: ")
    messages.append(prompt)

    if prompt=="0":
        break

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content[0]["text"])

print(messages)