# Feed the cleaned text to the LLM to generate flashcards.
# Using teh HuggingFace API to generate flashcards from the cleaned text.

from src.utils import load_text_file
from src.custom_exceptions import CustomException
from src.logger import logging as logger
import sys

from transformers.pipelines import pipeline

def generate_flashcards(text, model_name="google/flan-t5-base"):
    """
    Generates flashcards from cleaned text using a pre-trained model.
    
    Args:
        text (str): Cleaned text to generate flashcards from.
        model_name (str): Name of the pre-trained model to use for generation.
        
    Returns:
        list: List of generated flashcards.
    """
    try:
        logger.info("Initializing flashcard generation pipeline.")
        generator = pipeline("text2text-generation", model=model_name)
        
        logger.info("Generating flashcards from text.")
        prompt = (
            "Generate flashcards from the following text:\n"
            f"{text}\n\n"
            "Format each flashcard as a question and answer pair."
        )
        flashcards = generator(prompt, max_length=512, do_sample=True)
        
        logger.info("Flashcard generation completed successfully.") 
        return [fc['generated_text'] for fc in flashcards]
    
    except Exception as e:
        logger.error(f"Error during flashcard generation: {e}")
        raise CustomException(f"Failed to generate flashcards: {e}")

if __name__ == "__main__":
    try:
        # Example usage
        input_text = load_text_file("./artifacts/input_data/temp/cleaned_text.txt")
        flashcards = generate_flashcards(input_text)
        
        # Print the generated flashcards
        for i, card in enumerate(flashcards, 1):
            print(f"Flashcard {i}: {card}")
        
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")