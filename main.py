import sys

from stats import get_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_name = f.name
        file_contents = f.read()
        f.close()
    print(get_report(file_name, file_contents))



main()
