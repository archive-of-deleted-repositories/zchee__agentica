import os

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

def main():
    client = client = chromadb.CloudClient(
        api_key=os.getenv("CHROMA_API_KEY"),
        tenant=os.getenv("CHROMA_TENANT"),
        database=os.getenv("CHROMA_DATABASE")
    )

    openai_collection = client.create_collection(
        name="go-analysis-large",
        embedding_function=OpenAIEmbeddingFunction(
            model_name="text-embedding-3-large"
        ),
        configuration={"hnsw": {"space": "cosine"}}
    )
    print(openai_collection.id)

    # huggingface_ef = HuggingFaceEmbeddingFunction(
    #     api_key_env_var="HUGGINGFACE_API_KEY", model_name="Qwen/Qwen3-Embedding-8B"
    # )

    # collection = client.create_collection(
    #     name="go-analysis",
    #     embedding_function=openai_collection,
    # )
    # print(collection.id)

if __name__ == "__main__":
    main()
