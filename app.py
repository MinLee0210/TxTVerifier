import streamlit as st
from st_pages import Page, show_pages


st.set_page_config(
    layout="centered", page_title="Zero-Shot Text Classifier", page_icon="images/logo_00_transperancy.png"
)

show_pages(
    [
        Page("views/main.py", "Main Page"), 
        Page("views/about.py", "About"), 
        Page("views/contact.py", "Contact me")
    ]
)