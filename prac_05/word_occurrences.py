"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""

# Ask user for input
text = input("Text: ")

# Split the string into words
words = text.split()

# Create an empty dictionary to store word counts
word_counts = {}

# Count occurrences of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1  # If word is already in the dictionary, increment its count
    else:
        word_counts[word] = 1  # If word is not in the dictionary, add it with count 1

# Find the longest word to format the output properly
max_length = max(len(word) for word in word_counts)

# Sort the words and print them with counts in a formatted way
for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")