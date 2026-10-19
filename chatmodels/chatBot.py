# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI 
 
# load_dotenv()
# model = ChatMistralAI(model="mistral-small-2603")


# prompt=input("You:")
# response=model.invoke(prompt)

# print(response.content) 

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
print("choose your AI mode")
print("press 1 for angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")

choice=int(input("Tell your response :-"))

if choice==1:
    mode="You are an angry AI agent.You respond aggresively and impatiently."
elif choice==2:
    mode="You are very funny AI agent.You respond with jokes and humor."
elif choice==3:
    mode="You are sad AI agent.You respond with depressed and sadly."
messages=[
    SystemMessage(content=mode)

]
print("_ _ _ _ _ _ _ _ _ welcome type 0 to exit the application _ _ _ _ _ _ _ _ _")

while True:
    
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))

    if prompt=="0":
        break

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content[0]["text"])

print(messages)