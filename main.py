def main():
    filepath = 'books/frankenstein.txt'

    file_contents = get_contents(filepath)
    words = file_contents.split()
    characters = get_characters_dict(file_contents)

    print_report(filepath, words, characters)
    

def print_report(filepath: str, words: list, characters: dict):
    print(f"--- Begin Report for {filepath} ---")
    print(f"Found {len(words)} in the document")
    print()
    print("Character Counts:")
    for (k, v) in sorted(characters.items(), reverse=True, key=lambda x: x[1]):
        print(f"{k}: {v}")
    print(f"--- End Report for {filepath} ---")

def get_characters_dict(file_contents: str) -> dict:
    char_dict = {}
    for char in file_contents.lower():
        if not char.isalpha():
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_contents(filepath: str) -> str:
    with open(filepath) as f:    
        file_contents = f.read()
        return file_contents

if __name__ == "__main__":
    main()
