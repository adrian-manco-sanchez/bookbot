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
    
def count_characters(text: str) -> dict:
    """
    Count the frequency of each character in the given text.
    
    This function converts the input text to lowercase and counts the occurrence
    of each character, including spaces and punctuation marks.
    
    Args:
        text (str): The input text to analyze for character frequency.
        
    Returns:
        dict: A dictionary where keys are characters (lowercase) and values 
              are their respective counts in the text.
              
    Example:
        >>> count_characters("Hello World!")
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    """
    result = {}

    text = text.lower()
    for char in text:
        if char not in result.keys():
            result[char] = 1
            continue
        result[char] += 1

    return result