# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()
# embeddings=OpenAIEmbeddings(
#     model='text-embedding-3-large',
#     dimensions=64
# )

# vector=embeddings.embed_query("You are going to learn Gen  AI")

# print(vector)

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts=[
    "Hello this is rehan",
    "here we go again",
    "huh huhu hshh"
]
vector = embeddings.embed_documents(texts)

print(vector)
print(len(vector))