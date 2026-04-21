# streamlit Libraries
import streamlit as st

# nlp Libraries
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import re

# title
st.title("Sentiment Analysis App")
st.subheader("Enter text to analyze sentiment")

# user input
user_input = st.text_area("Enter your text here:")

# analyze button
if st.button("Analyze"):

    text = user_input

    # cleaning text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"http\S+", " link ", text)
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)

    # splitting text
    text = text.split()

    # lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)

    # sentiment analysis
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    result = sentiment_score

    # output
    if result > 0:
        st.success(f"Happy 😊 : {text}")
    elif result < 0:
        st.warning(f"Sad 😞 : {text}")
    else:
        st.info(f"Confused 😐 : {text}")

    st.success(f"Polarity Score is: {result}")

    