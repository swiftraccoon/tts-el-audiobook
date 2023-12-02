"""
This module handles the input operations for the audiobook converter.
It includes functionality to parse command line arguments and read
the input file.
"""

import argparse
import os


class InputHandler:
    """
    The InputHandler class is responsible for handling the input file.
    It parses command line arguments and validates the input file.
    """

    def get_file(self):
        """
        Parses command line arguments to get the file path,
        validates the file path, determines the file type,
        and reads the file content.
        Returns the file type and content.
        """
        parser = argparse.ArgumentParser(
            description="Process a file for audiobook conversion."
        )
        parser.add_argument('file_path', type=str,
                            help='Path to the file (PDF, epub, mobi)')
        parser.add_argument('--voice', type=str, default="Bella",
                            help='Voice to use for TTS')
        parser.add_argument('--model', type=str,
                            default="eleven_monolingual_v1",
                            help='Model to use for TTS')
        parser.add_argument('--debug', action='store_true',
                            help='Enable debug mode to save processed text')
        args = parser.parse_args()

        file_path = args.file_path
        
        # Validate file path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Validate file type
        valid_extensions = ['pdf', 'epub', 'mobi']
        file_extension = file_path.split('.')[-1].lower()
        if file_extension not in valid_extensions:
            raise ValueError(
                f"Unsupported file type: {file_extension}. "
                f"Supported types are: {', '.join(valid_extensions)}"
            )

        # Read file content
        with open(file_path, 'rb') as file:
            file_content = file.read()

        return file_extension, file_content, args.voice, args.model, args.debug
