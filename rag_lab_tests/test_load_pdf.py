import os
import pytest
from src.document_processing.load_pdf import load_pdf

@pytest.mark.asyncio
async def test_load_pdf():
    
    # Arrange    
    # Go up one level from the current file's directory
    parent_dir = os.path.dirname(os.path.dirname(__file__))

    # Build the path to the PDF file
    sample_pdf_path = os.path.join(parent_dir, "documents", "pdfs", "layout-parser-paper.pdf")

    # Act
    pages = await load_pdf(sample_pdf_path)

    # Assert
    assert isinstance(pages, list), "The result should be a list"
    assert len(pages) > 0, "The list should contain at least one page"

    # Check that each page is a valid Document object
    for page in pages:
        assert hasattr(page, "page_content"), "Each page should have page_content"
        assert hasattr(page, "metadata"), "Each page should have metadata"
