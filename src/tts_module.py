"""
This module interfaces with the Eleven Lab's Text-to-Speech API to convert
processed text into speech. It utilizes the Eleven Labs Python package for
API communication and response handling.
"""

from typing import Optional
from elevenlabs import generate, set_api_key


class TTSModule:
    """
    The TTSModule class is responsible for communicating with the Eleven Lab's
    Text-to-Speech API using the Eleven Labs Python package. It sends processed
    text and receives the audio data.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initializes the TTSModule with the necessary API key.

        Parameters:
        api_key (Optional[str]): The API key for accessing Eleven Lab's TTS API
                                 If None, it will use the environment variable
                                 ELEVEN_API_KEY or work with limited quota.
        """
        if api_key:
            set_api_key(api_key)

    def convert_to_speech(self, text: str, voice: str = "Alliana",
                          model: str = "eleven_monolingual_v1") -> bytes:
        """
        Converts the given text to speech using the Eleven Lab's TTS API.

        Parameters:
        text (str): The text to be converted to speech.
        voice (str): The voice to be used for speech synthesis.
        model (str): The model to be used for speech synthesis.

        Returns:
        bytes: The audio data received from the TTS API.
        """
        chunk_size = 5000  # Set the chunk size to the API limit
        chunks = [text[i:i+chunk_size] for i in range(
            0, len(text), chunk_size
        )]

        audio_data = []
        for chunk in chunks:
            audio_chunk = generate(text=chunk, voice=voice, model=model)
            audio_data.append(audio_chunk)

        # Combine the audio data from all chunks
        combined_audio = b''.join(audio_data)
        return combined_audio
