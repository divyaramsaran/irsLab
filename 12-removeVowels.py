text = "information retrieval system"

result = ""

for word in text.split():

    new_word = ""

    for ch in word:

        if ch.lower() not in "aeiou":
            new_word += ch

    result += new_word + " "

print("Original Text:", text)
print("Compressed Text:", result)