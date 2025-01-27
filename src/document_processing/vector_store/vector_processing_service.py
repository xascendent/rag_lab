from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

class VectorProcessingService:
    def __init__(self, config: dict):
        self.vector_store_embedding_model = config.get("model_options", {}).get("embedding_model", "text-embedding-3-small")
        self.vector_store_llm_model = config.get("model_options", {}).get("llm_model", "gpt-4o")
        self.vector_store_llm_temperature = config.get("model_options", {}).get("llm_temperature", 0.0)
        self.vector_store_llm_api_token_name = config.get("model_options", {}).get("llm_api_token_name", "OPENAI_API_KEY")


    def say_hello(self):
        print("Ready Player One")

    def create_vector_store(self, chunks: list):
        embeddings = OpenAIEmbeddings(model=self.vector_store_embedding_model)
        vector_store = FAISS.from_documents(chunks, embeddings)
        return vector_store


        
                

