import sys

from stats import get_book_text, count_words, count_characters, sort_character_count, generate_report

def main() -> None:
    """
    Entry point of the BookBot application.
    
    Reads a book file, counts the words, and displays the results.
    
    Args:
        args: Command line arguments, expects filepath as second argument.
    
    Returns:
        None
    """

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    book_word_count = count_words(book_text)
    book_character_count = count_characters(book_text)
    sorted_book_character_count = sort_character_count(book_character_count)

    generate_report(filepath, book_word_count, sorted_book_character_count)

if __name__ == "__main__":
    main()