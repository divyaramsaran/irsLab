from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Documents
documents = [
    "Python is a programming language",
    "Java is a programming language",
    "Machine learning uses Python",
    "Deep learning uses machine learning",
    "Java is used for software development"
]

# Convert documents into TF-IDF matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Apply LSI using SVD
lsi = TruncatedSVD(n_components=2)

result = lsi.fit_transform(X)

# Display results
print("Original Matrix:")
print(X.toarray())

print("\nLSI Matrix:")
print(result)

print("\nComponents:")
print(lsi.components_)