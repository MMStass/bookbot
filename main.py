from stats import count_words, count_characters, sorted_char_count
import sys

def main() -> int:

    path = handle_args()
    book = get_book_text(path_to_file=path)
    word_count = count_words(text=book)
    char_count = sorted_char_count(count_characters(text=book))

    print_results(word_count, char_count, path)
    
    return 0

def handle_args() -> str:

    if len(sys.argv) != 2:      
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return None
    
    else: 
        return sys.argv[1]

def get_book_text(path_to_file: str) -> str:
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: incorrect path: '{path_to_file}'")
        sys.exit(1)

    return file_contents

def print_results(word_count: int, char_count: list[dict[str,int]], path_to_book: str) -> int:

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in char_count:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

    return 0



main()