import gradio as gr
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load FAISS index and data
index = faiss.read_index("shl_faiss.index")
df = pd.read_pickle("shl_data.pkl")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Core recommendation logic
def recommend_assessments(query, top_k=5):
    query_emb = model.encode([query])
    faiss.normalize_L2(query_emb)
    D, I = index.search(query_emb, top_k)
    results = df.iloc[I[0]][['assesment_name', 'URL', 'remote_testing', 'Adaptive/IRT', 'duration', 'description']]
    return results.reset_index(drop=True)

# Gradio interface
with gr.Blocks(theme=gr.themes.Default()) as demo:
    gr.Markdown("# 🔍 SHL Assessment Recommender")
    gr.Markdown("Enter a job description or query below to get relevant SHL assessments.")

    query_input = gr.Textbox(label="Job Description or Query", placeholder="e.g., Java developers, collaboration, 40 minutes...")
    top_k_slider = gr.Slider(1, 10, value=5, step=1, label="Number of Recommendations")
    submit_btn = gr.Button("Get Recommendations")

    output_table = gr.Dataframe(label="Recommended Assessments", wrap=True)

    submit_btn.click(fn=recommend_assessments, inputs=[query_input, top_k_slider], outputs=output_table)

demo.launch()
