from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
categories = ['sci.space', 'comp.graphics']

train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

# Convert text into numerical vectors
vectorizer = TfidfVectorizer(stop_words='english')

X_train = vectorizer.fit_transform(train.data)
X_test = vectorizer.transform(test.data)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, train.target)

# Predict categories
predictions = model.predict(X_test)

# Display results
print("Actual Categories:", test.target[:10])
print("Predicted Categories:", predictions[:10])

print("Accuracy:", accuracy_score(test.target, predictions))