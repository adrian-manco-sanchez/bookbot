import sys

from stats import get_book_text, count_words, count_characters, sort_character_count, generate_report

FILEPATH = "books/frankenstein.txt"

def main(args=sys.argv) -> None:
    """
    Entry point of the BookBot application.
    
    Reads a book file, counts the words, and displays the results.
    
    Args:
        args: Command line arguments, expects filepath as second argument.
    
    Returns:
        None
    """

    book_text = get_book_text(FILEPATH)
    book_word_count = count_words(book_text)
    book_character_count = count_characters(book_text)
    sorted_book_character_count = sort_character_count(book_character_count)

    generate_report(FILEPATH, book_word_count, sorted_book_character_count)

if __name__ == "__main__":
    main()