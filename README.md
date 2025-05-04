# 🔍 SHL Assessment Recommendation System

A semantic search-based tool that recommends SHL assessments tailored to a given job description or role. Powered by SentenceTransformers, FAISS, and a streamlined Gradio UI, this system helps users find the most relevant SHL assessments in seconds.

---

## 📚 About the Project

This project simulates an SHL assessment recommendation engine. Users can input any job-related query, and the system returns top matching assessments based on the semantic similarity of their descriptions.

> ⚠️ **Note**: The dataset used in this project was synthetically generated using the `Faker` library. Due to JavaScript-based rendering and scraping restrictions on the SHL website, real-time data extraction was not feasible. Therefore, a fake dataset was created solely for demonstration and prototyping purposes.

---

## ✨ Features

- 🔍 Semantic search powered by `all-MiniLM-L6-v2`
- ⚡ High-speed similarity search using FAISS
- 🧾 Clean, table-formatted results in a user-friendly UI
- 🎛️ Customizable number of assessment recommendations
- 🚀 Deployable on Hugging Face Spaces with ease

---

## 🧠 How It Works

1. **Data Generation**: A mock dataset of SHL-like assessments is created using `Faker`, with fields such as name, duration, remote availability, and descriptions.
2. **Embedding**: Descriptions are converted into vector embeddings using a pre-trained sentence transformer (`all-MiniLM-L6-v2`).
3. **Indexing**: Embeddings are normalized and indexed using FAISS to support efficient similarity search.
4. **Recommendation**: User queries are embedded and compared with the indexed dataset to retrieve the most relevant assessments.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Tamannasinghk/SHL-Assessment-Recommender.git
cd SHL-Assessment-Recommender
```
### 2. Install the requirements

```bash
pip install -r requirements.txt
```
---
