"""
Word Occurrences
Estimate: 45 minutes
Actual: 1 hour
"""

text = input("Enter some words: ")
words = text.split()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
words = list(word_to_count.keys())
words.sort()
max_length = max(len(word) for word in list(word_to_count.keys()))+1
for word in words:
    print(f"{word:{max_length}}: {word_to_count[word]}")



