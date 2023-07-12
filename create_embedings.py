import numpy as np
from sentence_transformers import SentenceTransformer

def create_embeddings(model_path, texts):
    model = SentenceTransformer(model_path)
    embeddings = model.encode(texts)
    return embeddings

def save_embeddings(embeddings, file_path):
    np.save(file_path, embeddings)

def generate_and_save_embeddings():

    texts = [...]

    model_path = "model"

    embeddings = create_embeddings(model_path, texts)


    file_path = "data/embeddings.npy"
    save_embeddings(embeddings, file_path)

if __name__ == '__main__':
    generate_and_save_embeddings()
