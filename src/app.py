import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import json
from document_processing.document_processing_service import DocumentProcessingService

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

async def main():    
    config = load_config()
     
    document_processing_service = DocumentProcessingService(config)
    await document_processing_service.intake_documents()


if __name__ == "__main__":
    asyncio.run(main())
