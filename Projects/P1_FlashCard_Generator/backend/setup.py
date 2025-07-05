# To build our application as a package, we need to create a setup.py file.
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> list[str]:
    """
    This function reads the requirements from a file and returns them as a list.
    """
    requirements = []
    # Check if the file exists and read it
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .') # Remove editable install if present                
    return requirements


setup(
    name='FlashCardGenerator',
    version='1.0',
    author= 'Aakash Singh',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    description='A simple Flash Card Generator application that uses Hugging Face API to generate flash cards from text.'
)