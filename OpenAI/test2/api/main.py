from typing import Union
from fastapi import FastAPI, File

import openai
import deepl

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/traductor/{mp3_file}")
def read_item(mp3_file: str , q: Union[str, None] = None):
    
    audio_file= open(f"../../{mp3_file}", "rb")
    
    openai.api_key = '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'
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    file_convert = transcript["text"]
    
    auth_key = "4c4edf95-8ccc-93ec-a1fb-4503f21f0967:fx"  # Replace with your key
    translator = deepl.Translator(auth_key)
    
    result = translator.translate_text(file_convert, target_lang="FR")
    
    return {"traduction": result.text}