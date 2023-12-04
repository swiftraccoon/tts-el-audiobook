"""
This module handles the output operations for the audiobook converter.
It includes functionality to save the audio data received from the
Text-to-Speech API into an audio file.
"""


class AudioOutput:
    """
    The AudioOutput class is responsible for handling the audio data output.
    It saves the audio data into a file.
    """

    def save_audio_file(self, audio_data, filename='output_audio.mp3'):
        """
        Saves the audio data into an audio file.

        Parameters:
        audio_data (bytes): The audio data to be saved.
        filename (str): The name of the file to save the audio data.
                        Defaults to 'output_audio.mp3'.
        """
        with open(filename, 'wb') as file:
            file.write(audio_data)
        print(f"Audio file saved as {filename}")
