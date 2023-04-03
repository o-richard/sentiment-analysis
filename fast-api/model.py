import pickle

import nltk

# Obtain the model
filename = "sentiment_model.sav"
model, vectorizer = pickle.load(open(filename, "rb"))

# Obtain the English stopwords
nltk.download("stopwords")
nltk.download("punkt")
stopwords = set(nltk.corpus.stopwords.words("english"))


# Pre-process the text (Removal on non-alphanumeric words and stopwords)
def preprocess_text(text):
    """
    1. Convert the words to lower case
    2. Tokenize the words
    3. Ensure the words are alphanumeric
    4. Remove all stopwords
    """
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    words = [word for word in words if word not in stopwords]
    return " ".join(words)


def result(text):
    """
    Return either 0 (negative) or 4 (positive)
    """

    new_text = preprocess_text(text)
    new_text_vectorized = vectorizer.transform([new_text])
    sentiment = model.predict(new_text_vectorized)
    result = sentiment[0]
    # Ensure the result is of type int if possible
    try:
        result = int(result)
    except ValueError:
        pass
    return result
