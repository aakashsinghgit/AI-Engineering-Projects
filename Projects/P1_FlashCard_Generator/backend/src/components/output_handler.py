#Take outputs from the model and save it files - 5 flashcards
# This script saves the generated flashcards to a file after generating them from cleaned text.
# Using the HuggingFace API to generate flashcards from the cleaned text.

from src.utils import load_text_file
from src.logger import logging as logger
from src.custom_exceptions import CustomException
import sys
from fcard_generation import generate_flashcards

def save_flashcards_to_file(flashcards, output_file):
    """
    Saves the generated flashcards to a specified output file.
    
    Args:
        flashcards (list): List of generated flashcards.
        output_file (str): Path to the output file where flashcards will be saved.
    """
    try:
        logger.info(f"Saving {len(flashcards)} flashcards to {output_file}.")
        with open(output_file, 'w') as f:
            for card in flashcards:
                f.write(f"{card}\n")
        logger.info("Flashcards saved successfully.")
        
    except Exception as e:
        logger.error(f"Error saving flashcards to file: {e}")
        raise CustomException(f"Failed to save flashcards: {e}")
    
if __name__ == "__main__":
    try:
        # Load cleaned text from file
        input_text = load_text_file("./artifacts/input_data/temp/cleaned_text.txt")
        
        # Generate flashcards from the cleaned text
        flashcards = generate_flashcards(input_text)
        
        # Save the generated flashcards to a file
        output_file = "./artifacts/output_data/flashcards.txt"
        save_flashcards_to_file(flashcards, output_file)
        
        logger.info(f"Flashcards successfully generated and saved to {output_file}.")
        
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")