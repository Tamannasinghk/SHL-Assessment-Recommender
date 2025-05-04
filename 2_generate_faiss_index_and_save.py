import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Loading the dataset .
df = pd.read_csv("fake_shl_assessments.csv")

# Loading model for generating embeddings .
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generating description embeddings .
embeddings = model.encode(df['description'].tolist(), convert_to_numpy=True)

# Normalizing embeddings for cosine similarity .
faiss.normalize_L2(embeddings)

# Building FAISS index (cosine similarity) .
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

# Saving the index and dataframe .
faiss.write_index(index, "shl_faiss.index")
df.to_pickle("shl_data.pkl")
