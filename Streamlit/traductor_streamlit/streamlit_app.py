from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import openai
import deepl

"""
# Bienvenue sur traductor from audio

Evidemment cette API est un lien direct vers whisper OpenAI et DeepL :heart:
Ce streamlit est un exercice


"""
file = st.file_uploader("Upload a audio file to translate", type=["mp3"])

#response = requests.get(f"https://swapi.dev/api/{option}/").json()
st.write("a")
audio_file= open(file, "rb")
openai.api_key = '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'
st.write("1")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
st.write("2")
file_convert = transcript["text"]

st.write(file_convert)
