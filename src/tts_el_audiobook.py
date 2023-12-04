"""
This script is the main entry point for the audiobook converter.
It integrates various modules to convert a text file (PDF, epub, mobi)
into an audio file using the Eleven Labs Text-to-Speech API.
"""

import logging
import sys
from input_handler import InputHandler
from ai_processor import AIProcessor
from file_parser import FileParser
from text_processor import TextProcessor
from tts_module import TTSModule
from audio_output import AudioOutput

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')
# pylint: disable=logging-fstring-interpolation
def write_to_debug_file(filename, content):
    """
    Writes the given content to the specified file.
    Args:
        filename (str): name of file to write to
        content (str): content to write to file
    """
    with open(filename, 'w') as file:
        file.write(content)
        print(f"Debug file saved in {filename}")


def main():
    """
    Main function to orchestrate the conversion of text files to audio.
    It handles the entire process from file input to audio output.
    """
    try:
        input_handler = InputHandler()
        file_type, file_content, voice, model, debug = input_handler.get_file()
        logging.debug(f"[tts_el_audiobook] File type: {file_type}")
        logging.debug(f"[tts_el_audiobook] Voice: {voice}")
        logging.debug(f"[tts_el_audiobook] Model: {model}")
        logging.debug(f"[tts_el_audiobook] Debug: {debug}")

        parser = FileParser(file_type)
        text = parser.parse(file_content)
        logging.info(f"[tts_el_audiobook] Parsed text length: {len(text)}")

        processor = TextProcessor()
        processed_text = processor.process(text)
        logging.info(f"""
                     [tts_el_audiobook] Processed text length: {len(processed_text)}
                     """
                     )

        if debug == 'text':
            write_to_debug_file('text_debug.txt', processed_text)
            sys.exit()

        # ai_processor = AIProcessor(api_url="http://127.0.0.1:5000",
        #                            chunk_size=5000)
        # logging.debug(f"[tts_el_audiobook] AI processor URL: {ai_processor.api_url}")
        ai_processor = AIProcessor(api_key="sk-zz", model="gpt-3.5-turbo-16k-0613", chunk_size=16000)
        logging.debug(f"[tts_el_audiobook] AI processor chunk size: {ai_processor.chunk_size}")
        ai_processed_text = ai_processor.process_text(processed_text)
        logging.info(f"[tts_el_audiobook] AI processed text length: {len(ai_processed_text)}")

        if debug == 'ai':
            write_to_debug_file('text_debug.txt', processed_text)
            write_to_debug_file('ai_debug.txt', ai_processed_text)
            sys.exit()

        tts = TTSModule(api_key="zz")
        # logging.debug(f"[tts_el_audiobook] ElevenLabs TTS API key: {tts.api_key}")
        audio_data = tts.convert_to_speech(processed_text, voice, model)
        logging.info(f"[tts_el_audiobook] Audio data length: {len(audio_data)}")
        logging.debug(f"[tts_el_audiobook] Voice: {voice}")
        logging.debug(f"[tts_el_audiobook] Model: {model}")

        audio_output = AudioOutput()
        audio_output.save_audio_file(audio_data)

    except Exception as e:
        logging.error(f"[tts_el_audiobook] Error occurred: {e}")


if __name__ == "__main__":
    main()
