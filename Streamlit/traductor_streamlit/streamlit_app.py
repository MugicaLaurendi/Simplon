from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
"""
# Bienvenue sur mon API starwars

Evidemment cette API est un lien direct vers SWAPI :heart:
Ce streamlit est un exercice


"""

result_count = []




data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

response = requests.get(f"https://swapi.dev/api/{option}/").json()
