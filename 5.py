from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, f1_score, recall_score
from scipy.optimize import linear_sum_assignment
import numpy as np

categories = ['sci.space', 'comp.graphics']

data = fetch_20newsgroups(
    subset='train',
    categories=categories,
    remove=('headers', 'footers', 'quotes')
)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data.data)

model = KMeans(n_clusters = 2, random_state = 42, n_init = 10)
prediction = model.fit_predict(X)

actual = data.target

matrix = confusion_matrix(actual, prediction)

purity = np.array(np.max(matrix, axis=0)) / np.sum(matrix)

rows, cols = linear_sum_assignment(-matrix)
mapping = dict(zip(rows, cols))
prediction = np.array([mapping[x] for x in prediction])

precison = precision_score(actual, prediction, average='weighted')
recall = recall_score(actual, prediction, average='weighted')
fmeasure = f1_score(actual, prediction, average='weighted')

print('data:', len(data))
print('purity : ', purity)
print("precision :", precison)
print("recall : ", recall)
print("f1 score : ", fmeasure)