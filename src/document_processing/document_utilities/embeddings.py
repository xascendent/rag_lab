from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

async def embed_chunks_using_openAI(chunks: list[str], embedding_model: str, api_key: str) -> list[str]:    
    if not embedding_model:
        embedding_model = "text-embedding-3-small"
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:  # Ensure the API key is set
        raise ValueError("API key for OpenAI is missing. Set it in the .env file or pass it explicitly.")        
    
    embed = OpenAIEmbeddings(api_key=api_key, model=embedding_model)    
    print("Chunks to embed:", chunks)
    vectors = embed.embed_documents(chunks)    
    print(f"Number of vectors: {len(vectors)}")
    print(f"First vector: {vectors[0]}")
    print(f"Last vector: {vectors[-1]}")
    
    




if __name__ == "__main__":
    # Test code or example usage
    test_chunks = [
        "This is the first test chunk.",
        "This is the second test chunk.",
        "This is the third test chunk."
    ]

    embed_chunks_using_openAI(test_chunks, "text-embedding-3-small", os.getenv("OPENAI_API_KEY"))
