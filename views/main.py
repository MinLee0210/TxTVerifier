import requests
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_tags import st_tags  # to add labels on the fly!
from st_pages import add_page_title

from config import Config
from utils import query

# add_page_title()

# ----- From Navigation bar ----- 
st.sidebar.write("")

API_KEY = st.sidebar.text_input(
    "Enter your HuggingFace API key",
    help="Once you created you HuggingFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
    type="password",
)
API_OPTION = st.sidebar.selectbox(
    'Choose a model:',
    ("DistilBert", 
     "DistilRoBerta-Base", 
     "DeBerta", 
     "DistilBart", 
     "Bart-large"))
# Adding the HuggingFace API inference URL.
API_OPTION = API_OPTION.lower()
API_URL = Config.API_INFERENCE + Config.MODEL[API_OPTION]
print(API_URL)
# Now, let's create a Python dictionary to store the API headers.
headers = {"Authorization": f"Bearer {API_KEY}"}

st.sidebar.write(
    """
    App created by [Minh Le Duc](https://www.linkedin.com/in/minh-le-duc-a62863172/) using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/inference-api).
    """
)

# ----- From Main side -----
# We create a set of columns to display the logo and the heading next to each other.
c1, c2 = st.columns([0.32, 2])
with c1:
    st.image(
        "images/logo_02.jpg",
        width=85,
    )
with c2:
    st.caption("")
    st.title("Zero-Shot Text Classifier")

# We need to set up session state via st.session_state so that app interactions don't reset the app.
if not "valid_inputs_received" in st.session_state:
    st.session_state["valid_inputs_received"] = False
# Then, we create a intro text for the app, which we wrap in a st.markdown() widget.

st.write("")
st.markdown(
    """

Classify keyphrases on the fly with this mighty app. No training needed!

"""
)

st.write("")

# Now, we create a form via `st.form` to collect the user inputs.

# All widget values will be sent to Streamlit in batch.
# It makes the app faster!

with st.form(key="my_form"):
    labels_from_st_tags = st_tags(
        value=["Transactional", "Informational", "Navigational"],
        maxtags=3,
        suggestions=["Transactional", "Informational", "Navigational"],
        label="",
    )

    # MAX_KEY_PHRASES is a variable that controls the number of phrases that can be pasted:

    MAX_KEY_PHRASES = 50

    new_line = "\n"

    pre_defined_keyphrases = [
        "I want to buy something",
        "We have a question about a product",
        "I want a refund through the Google Play store",
        "Can I have a discount, please",
        "Can I have the link to the product page?",
    ]

    # Python list comprehension to create a string from the list of keyphrases.
    keyphrases_string = f"{new_line.join(map(str, pre_defined_keyphrases))}"

    # The block of code below displays a text area
    # So users can paste their phrases to classify

    text = st.text_area(
        # Instructions
        "Enter keyphrases to classify",
        # 'sample' variable that contains our keyphrases.
        keyphrases_string,
        # The height
        height=200,
        # The tooltip displayed when the user hovers over the text area.
        help="At least two keyphrases for the classifier to work, one per line, "
        + str(MAX_KEY_PHRASES)
        + " keyphrases max in 'unlocked mode'. You can tweak 'MAX_KEY_PHRASES' in the code to change this",
        key="1",
    )

    # The block of code below:

    # 1. Converts the data st.text_area into a Python list.
    # 2. It also removes duplicates and empty lines.
    # 3. Raises an error if the user has entered more lines than in MAX_KEY_PHRASES.

    text = text.split("\n")  # Converts the pasted text to a Python list
    linesList = []  # Creates an empty list
    for x in text:
        linesList.append(x)  # Adds each line to the list
    linesList = list(dict.fromkeys(linesList))  # Removes dupes
    linesList = list(filter(None, linesList))  # Removes empty lines

    if len(linesList) > MAX_KEY_PHRASES:
        st.info(
            f"Note that only the first "
            + str(MAX_KEY_PHRASES)
            + " keyphrases will be reviewed to preserve performance. Fork the repo and tweak 'MAX_KEY_PHRASES' in the code to increase that limit."
        )

        linesList = linesList[:MAX_KEY_PHRASES]

    submit_button = st.form_submit_button(label="Submit")

############ CONDITIONAL STATEMENTS ############

# Now, let us add conditional statements to check if users have entered valid inputs.
# E.g. If the user has pressed the 'submit button without text, without labels, and with only one label etc.
# The app will display a warning message.

if not submit_button and not st.session_state.valid_inputs_received:
    st.stop()

elif submit_button and not text:
    st.warning("There is no keyphrases to classify")
    st.session_state.valid_inputs_received = False
    st.stop()

elif submit_button and not labels_from_st_tags:
    st.warning("You have not added any labels, please add some! ")
    st.session_state.valid_inputs_received = False
    st.stop()

elif submit_button and len(labels_from_st_tags) == 1:
    st.warning("Please make sure to add at least two labels for classification")
    st.session_state.valid_inputs_received = False
    st.stop()

elif submit_button or st.session_state.valid_inputs_received:

    if submit_button:

        # The block of code below if for our session state.
        # This is used to store the user's inputs so that they can be used later in the app.

        st.session_state.valid_inputs_received = True

    ############ MAKING THE API CALL ############

    # First, we create a Python function to construct the API call.

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    # The function will send an HTTP POST request to the API endpoint.
    # This function has one argument: the payload
    # The payload is the data we want to send to HugggingFace when we make an API request

    # We create a list to store the outputs of the API call

    list_for_api_output = []

    # We create a 'for loop' that iterates through each keyphrase
    # An API call will be made every time, for each keyphrase

    # The payload is composed of:
    #   1. the keyphrase
    #   2. the labels
    #   3. the 'wait_for_model' parameter set to "True", to avoid timeouts!

    for row in linesList:
        api_json_output = query(
            {
                "inputs": row,
                "parameters": {"candidate_labels": labels_from_st_tags},
                "options": {"wait_for_model": True},
            }
        )

        # Let's have a look at the output of the API call
        # st.write(api_json_output)

        # All the results are appended to the empty list we created earlier
        list_for_api_output.append(api_json_output)

        # then we'll convert the list to a dataframe
        df = pd.DataFrame.from_dict(list_for_api_output)

    st.success("✅ Done!")

    st.caption("")
    st.markdown("### Check the results!")
    st.caption("")

    # st.write(df)

    ############ DATA WRANGLING ON THE RESULTS ############
    # Various data wrangling to get the data in the right format!

    # List comprehension to convert the score from decimals to percentages
    f = [[f"{x:.2%}" for x in row] for row in df["scores"]]

    # Join the classification scores to the dataframe
    df["classification scores"] = f

    # Rename the column 'sequence' to 'keyphrase'
    df.rename(columns={"sequence": "keyphrase"}, inplace=True)

    # The API returns a list of all labels sorted by score. We only want the top label.

    # For that, we need to select the first element in the 'labels' and 'classification scores' lists
    df["label"] = df["labels"].str[0]
    df["accuracy"] = df["classification scores"].str[0]

    # Drop the columns we don't need
    df.drop(["scores", "labels", "classification scores"], inplace=True, axis=1)

    # st.write(df)

    # We need to change the index. Index starts at 0, so we make it start at 1
    df.index = np.arange(1, len(df) + 1)

    # Display the dataframe
    st.write(df)

    cs, c1 = st.columns([2, 2])




    # The code below is for the download button
    # Cache the conversion to prevent computation on every rerun

    with cs:

        @st.cache_data
        def convert_df(df):
            return df.to_csv().encode("utf-8")

        csv = convert_df(df)

        st.caption("")

        st.download_button(
            label="Download results",
            data=csv,
            file_name="classification_results.csv",
            mime="text/csv",
        )