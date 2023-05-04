from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
"""
# Bienvenue sur traductor from audio

Evidemment cette API est un lien direct vers whisper OpenAI et DeepL :heart:
Ce streamlit est un exercice


"""

result_count = []

data = st.file_uploader("Upload a audio file to translate", type=["mp3"])

#response = requests.get(f"https://swapi.dev/api/{option}/").json()

print('data')
