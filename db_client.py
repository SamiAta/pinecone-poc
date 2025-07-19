import pinecone
import os
from dotenv import load_dotenv

load_dotenv()

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)
index = pinecone.Index(os.getenv("PINECONE_INDEX_NAME"))

def insert_vector(id: str, vector: list, metadata: dict):
    index.upsert([(id, vector, metadata)])

def search_vector(vector: list, top_k=5):
    return index.query(vector=vector, top_k=top_k, include_metadata=True)
