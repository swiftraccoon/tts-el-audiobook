"""
This script is the main entry point for the audiobook converter.
It integrates various modules to convert a text file (PDF, epub, mobi)
into an audio file using the Eleven Labs Text-to-Speech API.
"""

import logging
from input_handler import InputHandler
from file_parser import FileParser
from text_processor import TextProcessor
from tts_module import TTSModule
from audio_output import AudioOutput


def main():
    """
    Main function to orchestrate the conversion of text files to audio.
    It handles the entire process from file input to audio output.
    """
    try:
        input_handler = InputHandler()
        file_type, file_content, voice, model, debug_mode = input_handler.get_file()

        parser = FileParser(file_type)
        text = parser.parse(file_content)

        processor = TextProcessor()
        processed_text = processor.process(text)

        if debug_mode:
            with open('debug_processed_text.txt', 'w') as debug_file:
                debug_file.write(processed_text)
            print("Processed text saved in debug_processed_text.txt")
            return

        tts = TTSModule()
        audio_data = tts.convert_to_speech(processed_text, voice, model)

        audio_output = AudioOutput()
        audio_output.save_audio_file(audio_data)

    except Exception as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
