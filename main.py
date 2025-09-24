import sys

def count_words(text: str) -> int:
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The input text to count words from.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book from a text file.
    
    Args:
        filepath (str): The path to the text file containing the book.
    Returns:
        str: The content of the book as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main(args=sys.argv) -> None:
    """
    Entry point of the BookBot application.
    
    Reads a book file, counts the words, and displays the results.
    
    Args:
        args: Command line arguments, expects filepath as second argument.
    
    Returns:
        None
    """
    print("Hello! I am BookBot, your personal book assistant.")

    book_text = get_book_text("books/frankenstein.txt")
    book_word_count = count_words(book_text)
    print(f"Found {book_word_count} total words")

if __name__ == "__main__":
    main()