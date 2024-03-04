"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""


def count_word_occurrences(text):
    """
    Count occurrences of words in a string and print the results in sorted and aligned format.

    :param text: The input string.
    """
    word_counts = {}

    # Count occurrences of each word
    words = text.split()
    for word in words:
        # Remove punctuation (if any)
        word = word.strip(".,?!")
        # Convert to lowercase for case-insensitivity
        word = word.lower()

        # Update word count in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

    # Find the maximum width for formatting
    max_width = max(len(word) for word in word_counts)

    # Print the sorted and aligned results
    for word, count in sorted(word_counts.items()):
        print(f"{word:>{max_width}} : {count}")

user_input = input("Text: ")
count_word_occurrences(user_input)
