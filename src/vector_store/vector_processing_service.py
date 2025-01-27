from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

class VectorProcessingService:
    def __init__(self, config: dict):
        self.vector_store_embedding_model = config.get("model_options", {}).get("embedding_model", "text-embedding-3-small")
        self.vector_store_llm_model = config.get("model_options", {}).get("llm_model", "gpt-4o")
        self.vector_store_llm_temperature = config.get("model_options", {}).get("llm_temperature", 0.0)
        self.vector_store_llm_api_token_name = config.get("model_options", {}).get("llm_api_token_name", "OPENAI_API_KEY")


    


        
                

