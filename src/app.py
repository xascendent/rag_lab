import sys
import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import json
from document_processing.document_processing_service import DocumentProcessingService


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
