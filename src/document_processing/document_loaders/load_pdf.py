from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.schema import Document

async def load_pdf(file_path: str) -> list[Document]:
    loader = PyPDFLoader(file_path, extract_images=False)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    return pages    


async def load_json(file_path: str) -> list[Document]:
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents



