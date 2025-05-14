import sys
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
def main():
    from stats import count_words, count_characters, sort_characters, generate_report

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    # Word count
    num_words = count_words(book_text)
    # Character count and sorting
    char_count = count_characters(book_text)
    sorted_chars = sort_characters(char_count)
    # Generate report
    generate_report(filepath, num_words, sorted_chars)
main()