from bisect import bisect_left

# List of words
words = [
    "apple", "application", "apply",
    "banana", "ball", "bat",
    "computer", "compact", "car"
]

# Construct PAT array
pat_array = sorted(words)

print("PAT Array:")
print(pat_array)

# Prefix search
prefix = input("\nEnter prefix: ")

pos = bisect_left(pat_array, prefix)

print("\nMatching Words:")

found = False

for word in pat_array[pos:]:

    if word.startswith(prefix):
        print(word)
        found = True
    else:
        break

if not found:
    print("No matching words found")