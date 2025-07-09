# Takes the pdf file and extracts the text from it. 
# The text is then preprocessed to remove any unwanted characters,
# normalize whitespace, and convert to lowercase.
# The preprocessed text is saved as temporary file which can be readily used by the LLM.

from src.utils import save_text_file, load_pdf_file
from src.custom_exceptions import CustomException   
from src.logger import logging as logger
import sys

def clean_text(text):
    """
    Cleans text for LLM consumption, preserving all special characters (including those in formulae).
    - Lowercases text
    - Removes page numbers and extra whitespace
    """
    try:
        logger.info("Starting text cleaning.")
        # Lowercase
        text = text.lower()
        # Remove page numbers (lines that are just numbers)
        lines = text.splitlines()
        cleaned_lines = [line for line in lines if not line.strip().isdigit()]
        cleaned_text = ' '.join(cleaned_lines)
        # Remove extra whitespace
        cleaned_text = ' '.join(cleaned_text.split())
        logger.info("Text cleaning completed.")
        return cleaned_text.strip()
    except Exception as e:
        logger.error(f"Error during text cleaning: {e}")
        raise CustomException(e, sys) from e

def ingest_pdf(pdf_path, load_pdf_file):
    """
    Loads and cleans text from a PDF file.
    Args:
        pdf_path (str): Path to the PDF file.
        load_pdf_func (function): Utility function to extract text from PDF.
    Returns:
        str: Cleaned text ready for LLM.
    """
    try:
        logger.info(f"Loading PDF: {pdf_path}")
        raw_text = load_pdf_file(pdf_path)
        logger.info("PDF loaded successfully. Starting cleaning process.")
        cleaned_text = clean_text(raw_text)
        logger.info("PDF ingestion and cleaning successful.")
        return cleaned_text
    except Exception as e:
        logger.error(f"Error during PDF ingestion: {e}")
        raise CustomException(sys, e) from e
    
def save_cleaned_text(text, output_path):
    """
    Saves cleaned text to a file.
    Args:
        text (str): Cleaned text to save.
        output_path (str): Path to save the cleaned text file.
    """
    try:
        logger.info(f"Saving cleaned text to: {output_path}")
        save_text_file(output_path, text)
        logger.info("Cleaned text saved successfully.")
    except Exception as e:
        logger.error(f"Error saving cleaned text: {e}")
        raise CustomException(sys, e) from e

# Example usage:
# if __name__ == "__main__":  
#     try:
#         pdf_path = "artifacts/standard_pdfs/chapter_8.pdf"  # Replace with your PDF file path
#         output_path = "artifacts/input_data/temp/cleaned_text.txt"  # Replace with your desired output path
        
#         cleaned_text = ingest_pdf(pdf_path, load_pdf_file)
#         save_cleaned_text(cleaned_text, output_path)
        
#     except CustomException as e:
#         logger.error(f"Custom exception occurred: {e}")
#         raise CustomException(e, sys) from e