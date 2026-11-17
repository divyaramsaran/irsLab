import re

text = "Python is easy and Python is powerful"

words = re.findall(r'\b\w+\b', text.lower())

unique_words = set(words)

print("Total Terms:", len(words))
print("Unique Terms:", len(unique_words))

print("Unique Words:")
print(unique_words)