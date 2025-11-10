def main() -> int:

    print(get_book_text("./books/frankenstein.txt"))

    return 0


def get_book_text(path_to_file: str) -> str:

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents



main()