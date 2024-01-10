import streamlit as st
from st_pages import add_page_title

add_page_title()

# ----- Navigator content ----
# Let's add some info about the app to the sidebar.
st.sidebar.write(
    """
    App created by [Minh Le Duc](https://www.linkedin.com/in/minh-le-duc-a62863172/) using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/inference-api).
    """
)

# ----- Main content -----
st.subheader("About me")
st.markdown(
"""
    My name is Minh Le Duc, an AI enthusiast who is walking step by step on the path of becoming an expert in AI career. 
"""
)

st.subheader("About the project")
st.markdown(
"""
    Zero-shot learning (ZSL) is a branch of machine learning that tackles a challenging task: how to make models recognize things they've never seen before. 
    I like to look into its text classification capabilities in this project. 
    In specifics, users will specify the category details, and the agent will organize the text using the categories they provide without any additional training. 
"""
)

st.subheader("More details")
st.markdown(
"""
    More details about project structure and results of experiments are disscussed in the project's Github repo.
"""
)