def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    text = text.lower()
    characters = set()
    char_counts = {}

    for i in range(len(text)):
        characters.add(text[i])

    for c in characters:
        char_counts[c] = 0

    for i in range(len(text)):
        char_counts[text[i]] += 1

    return char_counts