"""
This module handles the parsing of different file types for
the audiobook converter.
It supports PDF, epub, and potentially other file formats.
"""

from io import BytesIO
from PyPDF2 import PdfReader
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


class FileParser:
    """
    The FileParser class is responsible for parsing the input file.
    It determines the appropriate method to parse based on the file type.
    """

    def __init__(self, file_type):
        """
        Initializes the FileParser with the specified file type.
        """
        self.file_type = file_type

    def parse(self, file_content):
        """
        Parses the file content based on the file type.
        Returns the extracted text from the file.
        """
        if self.file_type == 'pdf':
            return self.parse_pdf(file_content)
        if self.file_type == 'epub':
            return self.parse_epub(file_content)
        raise ValueError(f"Unsupported file type: {self.file_type}")

    def parse_pdf(self, content):
        """
        Parses PDF file content and extracts text using PdfReader.
        """
        # Create a file-like object from bytes
        file_stream = BytesIO(content)
        reader = PdfReader(file_stream)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return '\n'.join(text)

    def parse_epub(self, content):
        """
        Parses epub file content and extracts text.
        """
        book = epub.read_epub(content)
        text = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.content, 'html.parser')
                text.append(soup.get_text())
        return '\n'.join(text)

    # Implement other file type parsing methods if necessary
