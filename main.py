from stats import count_words, count_characters, sorted_char_count

def main() -> int:

    path = "./books/frankenstein.txt"

    book = get_book_text(path_to_file=path)

    word_count = count_words(text=book)
    
    char_count = sorted_char_count(count_characters(text=book))
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in char_count:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")


    return 0

def get_book_text(path_to_file: str) -> str:

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents





main()