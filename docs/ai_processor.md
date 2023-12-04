# AI Processor Module ([ai_processor.py](https://github.com/swiftraccoon/tts-el-audiobook/blob/main/tts_el_audiobook/ai_processor.py))

## Description:
This module, `AIProcessor`, handles the interaction with OpenAI's API. It is designed to process text in chunks that are suitable for the context limits of large language models (LLMs).

## Key Features:
- Initialization with OpenAI API key and model selection.
- Text processing in manageable chunks using OpenAI's ChatGPT API.
- Handles chunking of text to fit within API limits.
- Logging of processing steps for debugging and monitoring.

## Enhancement Ideas:
- Implement error handling for API request failures.
- Add support for different OpenAI models and customizable settings.
- Integrate a caching mechanism to avoid reprocessing identical text chunks.
- Provide a feature for asynchronous processing of large text batches.

## Misc Thoughts:
- The class structure is well-defined and focused on its purpose.
- The use of logging is a good practice, but it could be enhanced with different log levels.
- The hard-coded model and chunk size in the `__init__` method could be made more flexible.
- Exception handling could be more robust, especially around the API calls.

