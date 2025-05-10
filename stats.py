from typing import Dict

def get_number_of_words(book: str) -> int:
    """Splits the book string into words to count total number of words"""
    return len(book.split())


def get_number_of_chars(book: str) -> Dict[str, int]:
    """
    - Traverses through the lower-cased book string.
    - For every traversed character in the string:
        - If found first time char_map, add it
        - Else, increment it by 1
    """
    char_map = dict()
    for ch in book.lower():
        if ch not in char_map.keys():
            char_map[ch] = 1
        else:
            char_map[ch] += 1
    return char_map


def get_report(book_name: str, book: str) -> str:
    """"""
    header = "\
============ BOOKBOT ============\n\
Analyzing book found at {}...\n\
----------- Word Count ----------\n\
Found {} total words\n\
--------- Character Count -------\n\
".format(book_name, get_number_of_words(book))
    body = ""
    book_char_map = get_number_of_chars(book)
    for char, count in sorted(
        book_char_map.items(), key=lambda item: item[1], reverse=True
    ):
        if char.isalpha():
            body += "{}: {}\n".format(char, count)
    footer = "============= END ==============="

    return header + body + footer
