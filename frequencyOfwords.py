from collections import Counter

text = "I love Python and I love programming"

stop_words = {"i", "am", "is", "the", "and", "a"}

words = text.lower().split()

result = []

for word in words:

    if word not in stop_words:
        result.append(word)

frequency = Counter(result)

print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)