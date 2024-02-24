from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

stan = np.load("data/stan.npy", allow_pickle=True)
stan_embeddings = np.load("data/stan_embeddings.npy", allow_pickle=True)


def get_embedding(text):
    inputs = tokenizer(
        text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()


def respond(query):
    query_embedding = get_embedding(query)
    similarity = cosine_similarity(np.vstack(stan_embeddings), query_embedding)
    most_similar_index = similarity.argmax()
    return stan[most_similar_index], similarity[most_similar_index]
