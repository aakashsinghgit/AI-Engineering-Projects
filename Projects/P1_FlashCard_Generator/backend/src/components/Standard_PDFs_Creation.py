# Splitting a big pdf file into 8 small pdfs - chapter wise, which will be used to create flashcards as standard available samples.
from pypdf import PdfReader, PdfWriter
from pathlib import Path
import re

from src.custom_exceptions import CustomException
from src.logger import logging

def find_chapter_starts(pdf_path: str) -> list:
    """
    Finds the starting pages of each chapter in the PDF based on the chapter title pattern.
    """
    try:
        reader = PdfReader(pdf_path)
        chapter_starts = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and re.search(r'Chapter\s+\d+', text):
                chapter_starts.append(i)
        logging.info(f"Found {len(chapter_starts)} chapters in the PDF.")
        return chapter_starts
    except Exception as e:
        logging.error(f"Error finding chapter starts in PDF: {e}")
        raise CustomException(f"Error finding chapter starts: {e}")
    
def split_pdf_by_chapters(pdf_path: str, output_dir: str) -> None:
    """
    Splits the PDF into smaller PDFs based on chapter starts.
    """
    try:
        reader = PdfReader(pdf_path)
        chapter_starts = find_chapter_starts(pdf_path)
        
        if not chapter_starts:
            logging.warning("No chapters found in the PDF.")
            return
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for i in range(len(chapter_starts)):
            start_page = chapter_starts[i]
            end_page = chapter_starts[i + 1] if i + 1 < len(chapter_starts) else len(reader.pages)
            writer = PdfWriter()
            
            for j in range(start_page, end_page):
                writer.add_page(reader.pages[j])
            
            output_file = output_dir / f"chapter_{i + 1}.pdf"
            with open(output_file, 'wb') as f:
                writer.write(f)
                
            logging.info(f"Saved {output_file} with pages {start_page + 1} to {end_page}.")
    except Exception as e:
        logging.error(f"Error splitting PDF by chapters: {e}")
        raise CustomException(f"Error splitting PDF: {e}")

# if __name__ == "__main__":
#     pdf_path = "artifacts/standard_pdfs/Tlbdl.pdf" 
#     output_dir = "artifacts/standard_pdfs"
    
#     try:
#         split_pdf_by_chapters(pdf_path, output_dir)
#         logging.info("PDF splitting completed successfully.")
#     except CustomException as e:
#         logging.error(f"An error occurred: {e}")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")

# There is a bug in this logic, as it split few chapters into 2-3 parts becasue they mention that in next chapters (Like - Chapter 4) we will discuss this.
# This needs to be fixed by checking the next page text as well.
# This is a temporary solution to split the pdf into chapters, which will be used to create flashcards as standard available samples.
# The final solution will be to use a more robust method to identify chapter starts, such as using a more sophisticated text analysis or machine learning model to identify chapter titles and their corresponding pages.
# This will be implemented in the future.
# For now let's use Chapter 7 with 39 pages, Chapter 8 as 18 pages - as the standard sample pdf to create flashcards.It is well extracted.

     