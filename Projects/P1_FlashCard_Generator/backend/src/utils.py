# Creating utility functions for the backend with 4 functions: save and load for pdf and text.

import os
import sys
from pypdf import PdfReader
from pathlib import Path

from src.logger import logging
from src.custom_exceptions import CustomException

def save_text_file(file_path: str, content: str) -> None:
    """
    Saves the given content to a text file at the specified file path.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Text file saved successfully at {file_path}")
    except Exception as e:
        logging.error(f"Error saving text file at {file_path}: {e}")
        raise CustomException(sys, e) from e
    
def load_text_file(file_path: str) -> str:
    """
    Loads the content from a text file at the specified file path.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        logging.info(f"Text file loaded successfully from {file_path}")
        return content
    except Exception as e:
        logging.error(f"Error loading text file from {file_path}: {e}")
        raise CustomException(sys, e) from e

def save_pdf_file(file_path: str, content: str) -> None:
    """
    Saves the given content to a PDF file at the specified file path.
    """
    try:
        pdf = PdfReader()
        pdf.add_page()
        pdf.pages[0].insert_text(content)
        with open(file_path, 'wb') as file:
            pdf.write(file)
        logging.info(f"PDF file saved successfully at {file_path}")
    except Exception as e:
        logging.error(f"Error saving PDF file at {file_path}: {e}")
        raise CustomException(sys, e) from e
    
def load_pdf_file(file_path: str) -> str:
    """
    Loads the content from a PDF file at the specified file path.
    """
    try:
        pdf = PdfReader(file_path)
        content = ''
        for page in pdf.pages:
            content += page.extract_text() + '\n'
        logging.info(f"PDF file loaded successfully from {file_path}")
        return content
    except Exception as e:
        logging.error(f"Error loading PDF file from {file_path}: {e}")
        raise CustomException(sys, e) from e



