from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

doc1 = "I Love Python"
doc2 = "I Love JAVASCRIPT"

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform([doc1, doc2])

similarity = cosine_similarity(vectors[0], vectors[1])

print("Array Vectors:")
print(vectors.toarray())

print("Similarity:")
print(similarity[0][0])