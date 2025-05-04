from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# Loading FAISS index and dataset .
index = faiss.read_index("shl_faiss.index")
df = pd.read_pickle("shl_data.pkl")

# Loading model for generating embeddings .
model = SentenceTransformer("all-MiniLM-L6-v2")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5  # Setting default number of recommendations as 5 .

def recommend_assessments(user_input, top_k=5):
    # Converting input to embedding .
    query_emb = model.encode([user_input])
    faiss.normalize_L2(query_emb)

    # Searching in FAISS index .
    D, I = index.search(query_emb, top_k)
    
    # Getting results from DataFrame based on indices .
    results = df.iloc[I[0]][['assesment_name', 'URL', 'remote_testing', 'Adaptive/IRT', 'duration', 'description']]
    return results

@app.post("/recommendations/")
async def get_recommendations(request: QueryRequest):
    try:
        recommendations = recommend_assessments(request.query, request.top_k)
        # Converting results to dictionary for easy response .
        recommendations_list = recommendations.to_dict(orient='records')
        return {"recommendations": recommendations_list}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))