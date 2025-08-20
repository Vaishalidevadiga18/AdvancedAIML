import nltk
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')


sentence = "Python programming using libraries is very powerful!"
tokens = word_tokenize(sentence)

print("Tokens:", tokens)
