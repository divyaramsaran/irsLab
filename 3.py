from sklearn.datasets import fetch_20newsgroups
import re

# Import dataset
data = fetch_20newsgroups(subset='train')

documents = data.data[:50]

# Construct inverted index
inverted_index = {}

for i, text in enumerate(documents):

    words = re.findall(r'\b[a-z]+\b', text.lower())
    doc_id = "D" + str(i + 1)

    for word in words:

        if word not in inverted_index:
            inverted_index[word] = []

        if doc_id not in inverted_index[word]:
            inverted_index[word].append(doc_id)

# Display results
print("Total Documents:", len(documents))
print("Total Vocabulary:", len(inverted_index))

print("\nInverted Index:")

for word, doc_ids in inverted_index.items():
    print(word, ":", doc_ids)