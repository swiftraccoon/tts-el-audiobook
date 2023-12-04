"""
This module handles the processing of text extracted from various file formats
for the audiobook converter. It includes functionality to clean and prepare
the text for text-to-speech conversion.
"""


class TextProcessor:
    """
    The TextProcessor class is responsible for processing the extracted text.
    It performs operations such as cleaning and formatting the text.
    """

    def process(self, text):
        """
        Processes the extracted text.
        Performs operations like trimming whitespace, removing unnecessary
        characters, and other text formatting tasks.

        Parameters:
        text (str): The extracted text to be processed.

        Returns:
        str: The processed text.
        """
        processed_text = text.strip()
        return processed_text
