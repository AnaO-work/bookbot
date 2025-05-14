def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the occurrences of each character in the text.
    Converts all characters to lowercase to avoid duplicates.
    
    Returns:
        dict: A dictionary where the key is a character and the value is the count.
    """
    char_count = {}
    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_characters(char_dict):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary has two key-value pairs: 'char' and 'num'.
    
    Args:
        char_dict (dict): Dictionary with characters as keys and their counts as values.

    Returns:
        list: A sorted list of dictionaries from greatest to least by count.
    """
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list


def generate_report(filepath, word_count, sorted_chars):
    """
    Generates and prints a report of the word count and character frequencies.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

