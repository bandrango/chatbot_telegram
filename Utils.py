import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

lemmer = nltk.stem.WordNetLemmatizer()
ptemmer = PorterStemmer()

# Clear the corpus
def clear_corpus(text):
    text = nltk.word_tokenize(text)
    text = list(filter(lambda text: text not in string.punctuation, text))
    text = [ptemmer.stem(word.lower()) for word in text]
    return text

# Apply WordNetLemmatizer to the text.
def LemTokens(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(token) for token in tokens] 

# Apply word_tokenize to the text.
def Normalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))