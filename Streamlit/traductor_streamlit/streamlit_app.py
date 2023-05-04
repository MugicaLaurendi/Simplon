from collections import namedtuple
import altair as alt
import streamlit as st
import openai
import deepl

"""
# Bienvenue sur traductor from audio

Evidemment cette API est un lien direct vers whisper OpenAI et DeepL :heart:
Ce streamlit est un exercice


"""
file = st.file_uploader("Upload a audio file to translate", type=["mp3"])

#response = requests.get(f"https://swapi.dev/api/{option}/").json()
if file is not None :
    st.write(file)
    st.write("a")
    audio_file= open(file, "rb")
    st.write("b")
    openai.api_key = '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'
    st.write("1")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    st.write("2")
    file_convert = transcript["text"]

    st.write(file_convert)
