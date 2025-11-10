from stats import count_words, count_characters

def main() -> int:

    book = get_book_text("./books/frankenstein.txt")

    word_count = count_words(text=book)
    
    char_count = count_characters(text=book)
    
    print(f"Found {word_count} total words")
    
    for k, v in char_count.items():
        print(f"'{k}': {v}")

    return 0

def get_book_text(path_to_file: str) -> str:

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents



main()