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

st.write("Hi 👋, I'm Letlhogonolo Mothoagae")
st.write("""Final-year BSc Computer Science & Electronics student | Full-Stack Developer | Systems & Automation Builder
I design and build practical digital systems that help businesses operate better — from web platforms and automation workflows to secure, scalable system architectures.""")

st.divider()

st.title("About Me")
st.write("🎓 Final-year BSc Computer Science & Electronics student (South Africa)")
st.write("🏗️ Founder & Developer at Plug Connect Solutions — a digital solutions and systems development initiative")
st.write("🔍 Strong interest in Full-Stack Development, Cybersecurity Awareness, Cloud Computing, Networks, and Business Automation")
st.write("🧠 I focus on how systems work end-to-end, not just writing code")
st.write("🏆 Actively building competition-ready and client-ready prototypes")


st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")


st.write("visit us @Plug Connect Solutions")



