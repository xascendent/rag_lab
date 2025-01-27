import os
import sys
import asyncio
from datetime import datetime
import shutil
import json

# document 
from .document_loaders.load_pdf import load_pdf, load_json
from .document_utilities.embeddings import embed_chunks_using_openAI
from .document_utilities.splitter import chunk_pdf_document
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# vector store
from vector_store.hello import say_hello
#from src.vector_store.hello import say_hello
#from document_utilities.embeddings import embed_chunks_using_openAI
#from document_loaders.load_pdf import load_pdf, load_json
#from document_utilities.splitter import chunk_pdf_document

# vector store
#from vector_store.vector_processing_service import VectorProcessingService


class DocumentProcessingService:
    def __init__(self, config: dict):

       # Document section
        self.chunk_size = config.get("document_loader", {}).get("chunking", {}).get("chunk_size", 1000)
        self.chunk_overlap = config.get("document_loader", {}).get("chunking", {}).get("chunk_overlap", 200)
        self.file_intake_pdf_locations = config.get("document_loader", {}).get("file_processing_locations", {}).get("pdf", [])
        self.file_intake_json_locations = config.get("document_loader", {}).get("file_processing_locations", {}).get("json", [])

        # Model section
        self.llm_model = config.get("model_options", {}).get("llm_model", "gpt-4o")
        self.llm_temperature = config.get("model_options", {}).get("llm_temperature", 0.0)
        self.llm_api_token_name = config.get("model_options", {}).get("llm_api_token_name", "OPENAI_API_KEY")
        self.api_key = os.getenv(self.llm_api_token_name)
        self.embedding_model = config.get("model_options", {}).get("embedding_model", "text-embedding-3-small")

    async def intake_documents(self):
        # testing hello
        say_hello()
        # Load PDFs and JSON files
        await self.process_pdf_files()
        await self.process_json_files()
    
    async def process_files(self, file_locations, loader_function, embedder_function, chunk_size, chunk_overlap, embedding_model, api_key, file_extension):
        for file_location in file_locations:
            path = file_location["landing_path"]  # Extract the actual path
            processed_path = file_location["processed_path"]

            files = [f for f in os.listdir(path) if f.endswith(file_extension)]  # List files with the given extension
            print(f"{file_extension.upper()} files found in {path}: {files}")

            if files:
                for file in files:
                    file_path = os.path.join(path, file)
                    documents = await loader_function(file_path)

                    # Append new metadata
                    for doc in documents:
                        doc.metadata["process_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Chunk and embed
                    chunks = await chunk_pdf_document(documents, chunk_size, chunk_overlap)
                    await embedder_function(chunks, embedding_model, api_key)

                    # Move the processed file
                    shutil.move(file_path, processed_path)

    async def process_pdf_files(self):
        await self.process_files(
            self.file_intake_pdf_locations,
            load_pdf,
            embed_chunks_using_openAI,
            self.chunk_size,
            self.chunk_overlap,
            self.embedding_model,
            self.api_key,
            ".pdf"
        )

    async def process_json_files(self):
        await self.process_files(
            self.file_intake_json_locations,
            load_json,
            embed_chunks_using_openAI,
            self.chunk_size,
            self.chunk_overlap,
            self.embedding_model,
            self.api_key,
            ".json"
        )


# Issue running from app.py - need to fix
def load_config():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to config.json
    config_path = os.path.join(current_dir, 'config.json')

    # Open and load the JSON file
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config
    

async def main():    
    config = load_config()
     
    document_processing_service = DocumentProcessingService(config)
    await document_processing_service.intake_documents()

    #vector_processing_service = VectorProcessingService(config)
    #vector_processing_service.say_hello()



if __name__ == "__main__":
    asyncio.run(main())
