"""
Word Occurrences
Estimate: 45 minutes
Actual:
"""

text = "this is a collection of words of nice words this is a fun thing it is"
print(text)
words = text.split()
print(words)
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
print(word_to_count)
words = list(word_to_count.keys())
print(words)
for word, count in word_to_count.items():
    print(f"{word}: {count}")



