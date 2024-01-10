
<br />
<div align="center">
  <a href="https://github.com/MinLee0210/TxTVerifier.git">
    <img src="images/logo_02.jpg" alt="Logo" width="120" height="120">
  </a>

<h3 align="center">Zero-shot text classification</h3>

  <p align="center">
    Applying zero-shot learning on classification task.
    <br/>
  </p>
</div>

## About the project
Zero-shot learning (ZSL) is a branch of machine learning that tackles a challenging task: how to make models recognize things they've never seen before. I like to look into its text classification capabilities in this project. In specifics, users will specify the category details, and the agent will organize the text using the categories they provide without any additional training. 

To make inference, I use `huggingface` API inference. Therefore, downloading models to local directory is not neccessary. Making the application more light-weighted and easy to use. 
## Getting started
### Setup
You should clone the project and install its requirements. The action can be done by the below instructions: 
```
    git clone https://github.com/MinLee0210/TxTVerifier.git
    cd TxtVerifier
    pip install -r requirements.txt
```
## Usage
To begin with, you run this command line, remember that the dir must point to the project
`
    streamlit run app.py
`
From the UI, you must set your `huggingface` API key to access its API. After that, you can freely choose any models that are introduced. Following the process, You can set these labels anything, e.g.:

- `Positive`, `Negative` and `Neutral` for sentiment analysis
- `Angry`, `Happy`, `Emotional` for emotion analysis
- `Navigational`, `Transactional`, Informational for intent classification purposes
- Your product range (`Bags`, `Shoes`, `Boots` etc.)

## Gallery
An UI from Main page
![](/images/main_page.png)

## Acknowledgement
My code is heavily inspired by [an incredible source](https://github.com/streamlit/example-app-zero-shot-text-classifier.git) that I found on [Streamlit Gallery](https://streamlit.io/gallery). 