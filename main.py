from typing import Dict


def main():
    with open("books/frankenstein.txt") as f:
        file_name = f.name
        file_contents = f.read()
        f.close()
    print(get_number_of_words(file_contents))
    print(get_number_of_chars(file_contents))
    print(get_report(file_name, file_contents))


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
    header = "--- Begin report of {} ---\n".format(book_name)
    sub_header = "{} words found in the\
                   document\n\n".format(get_number_of_words(book))
    body = ""
    book_char_map = get_number_of_chars(book)
    for char, count in sorted(
        book_char_map.items(), key=lambda item: item[1], reverse=True
    ):
        if char.isalpha():
            body += "The '{}' character was found {} times\n".format(char, count)
    footer = "--- End report ---"

    return header + sub_header + body + footer


main()
