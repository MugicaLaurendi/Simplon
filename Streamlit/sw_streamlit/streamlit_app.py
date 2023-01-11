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

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

"""

result_count = []

option = st.selectbox(
    'Choose category :',
    ('','people', 'starships', 'planets'))

response = requests.get(f"https://swapi.dev/api/{option}/").json()


if option != '' :

    ###

    searched = st.text_input(f"Search in {option}")

    st.write(f'{len(result_count)} results')


    for i in response["results"] :

        if searched != '' :

            name = i["name"].lower()
            is_in = name.find(searched)

            if is_in >= 0 :
                result_count.append(i["name"])
                st.write("---------------")

                for y in i :

                    if y == "name" :
                        st.write(f"### {i[y]}")

                    else :
                        st.write(f"{y} : {i[y]}")
        else :
            result_count.append(i["name"])
            st.write("---------------")

            for y in i :

                    if y == "name" :
                        st.write(f"### {i[y]}")

                    else :
                        st.write(f"{y} : {i[y]}")
