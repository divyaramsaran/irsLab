import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

text = "I am a Student"

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

stemmer = PorterStemmer()

result = []

for word in words:
    if word.lower() not in stop_words:
        result.append(stemmer.stem(word))

print("Preprocessed result:")
print(result)