import streamlit as st
from st_pages import add_page_title

add_page_title()


st.sidebar.write("")


# Let's add some info about the app to the sidebar.
st.sidebar.write(
    """
    App created by [Minh Le Duc](https://www.linkedin.com/in/minh-le-duc-a62863172/) using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/inference-api).
    """
)

st.markdown("""

    + Gmail: minh.leduc.0210@gmail.com
    + Linkedin: https://www.linkedin.com/in/minh-le-duc-a62863172/
    + Github: https://github.com/Octo-Opt

""")