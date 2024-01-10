class Config: 
    API_INFERENCE="https://api-inference.huggingface.co/models/"
    MODEL = {
        "distilbart": "valhalla/distilbart-mnli-12-3",
        "distilroberta-base": "cross-encoder/nli-distilroberta-base", 
        "distilbert": "AyoubChLin/DistilBERT_ZeroShot", 
        "deberta": "MoritzdLaurer/deberta-v3-base-zeroshot-v1", 
        "bart-large": "facebook/bart-large-mnli", 
    }