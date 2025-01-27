from langchain_text_splitters import CharacterTextSplitter
from langchain.schema import Document


# TODO: Add a function to chunk json documents currently i'm using the PDF to do this but we will want to parse the json out a bit so we don't only pull part of a visit since it wouldn't make sense to embed a partial visit and the other part with someone else's visit
async def chunk_pdf_document(document: list[Document], chunk_size: int, chunk_overlap: int) -> list[str]:
    splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    docs = splitter.split_documents(document)
    # Extract page_content (text) from each Document object
    chunks = [doc.page_content for doc in docs]

    print("Pages in the original document: ", len(document))
    print("Length of chunks after splitting pages: ", len(chunks))

    return chunks