# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.title("Profile Page with Projects made in Github")

# Collect basic information
name = "Letlhogonolo Mothoagae"
field = "Full Stack Developer"
institution = "North West University"

st.image(
    "https://avatars.githubusercontent.com/u/122881376?s=400&u=5f7bc907ff8fbdbc51ca1e230ae617d0eabb6f18&v=4",
    caption="Github Profile picture"
)

st.write("Hello2")

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")


st.write("visit us @Plug Connect Solutions")

