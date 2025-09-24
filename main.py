import sys

from stats import get_book_text, count_words

def main(args=sys.argv) -> None:
    """
    Entry point of the BookBot application.
    
    Reads a book file, counts the words, and displays the results.
    
    Args:
        args: Command line arguments, expects filepath as second argument.
    
    Returns:
        None
    """

    book_text = get_book_text("books/frankenstein.txt")
    book_word_count = count_words(book_text)
    print(f"Found {book_word_count} total words")

if __name__ == "__main__":
    main()