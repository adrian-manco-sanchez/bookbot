# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project! It's a command-line text analysis tool that reads book files and generates comprehensive statistics about their content.

## Features

- **Word Count**: Counts the total number of words in a text file
- **Character Frequency Analysis**: Analyzes and counts the frequency of each alphabetic character
- **Detailed Reports**: Generates formatted reports with word count and character frequency statistics
- **Command-line Interface**: Easy-to-use CLI for processing book files

## Usage

Run BookBot by providing the path to a text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
h: 19725
r: 18557
d: 16863
============= END ===============
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Project Structure

```
bookbot/
├── main.py         # Main entry point and CLI interface
├── stats.py        # Text analysis functions and utilities
└── README.md       # Project documentation
```

## Functions

### `main.py`
- `main()`: Entry point that handles command-line arguments and orchestrates the analysis

### `stats.py`
- `get_book_text(filepath)`: Reads text content from a file
- `count_words(text)`: Counts the total number of words
- `count_characters(text)`: Counts character frequency (case-insensitive)
- `sort_character_count(character_count)`: Sorts characters by frequency in descending order
- `generate_report(filepath, word_count, sorted_character_count)`: Displays formatted analysis results

## About

This project was created as part of the [Boot.dev](https://www.boot.dev) Python curriculum. It demonstrates fundamental programming concepts including:

- File I/O operations
- String manipulation and parsing
- Data structures (dictionaries and lists)
- Sorting and data analysis
- Command-line argument processing
- Function organization and modularity