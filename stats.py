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