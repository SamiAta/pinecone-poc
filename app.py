from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
from embedder import get_embedding
from db_client import insert_vector, search_vector

app = FastAPI()

class InsertRequest(BaseModel):
    text: str
    metadata: dict = {}

class SearchRequest(BaseModel):
    text: str
    top_k: int = 5

@app.post("/insert")
def insert(req: InsertRequest):
    vector = get_embedding(req.text)
    insert_vector(str(uuid.uuid4()), vector, req.metadata)
    return {"status": "inserted"}

@app.post("/search")
def search(req: SearchRequest):
    try:
        vector = get_embedding(req.text)
        results = search_vector(vector, req.top_k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
