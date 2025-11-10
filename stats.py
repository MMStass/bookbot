def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    
    text = text.lower()
    
    characters = set()
    
    char_counts = {}

    for character in text:
        if character.isalpha():
            characters.add(character)

    for c in characters:
        char_counts[c] = 0

    for character in text:
        if character.isalpha():
            char_counts[character] += 1

    return char_counts

def sort_on(items: dict) -> int:
    return items["num"]

def sorted_char_count(dict: dict[str, int]) -> list[dict[str, int]]:
    result = []
    for k, v in dict.items():
        result.append({"char": k, "num": v})
    result.sort(reverse=True, key=sort_on)
    return result