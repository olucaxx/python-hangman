def get_words_list() -> list[str]:
    with open("words.txt") as file:
        return [line.strip() for line in file]


def update_words_file(words: list[str]) -> None:
     with open("words.txt", "w") as file:
         for word in words:
            file.write(f"{word}\n")


def print_words(words: list[str]) -> None:
    for index, word in enumerate(words, start=1):
        print(f"{index}. '{word}'")
        

def add_new_words(new_words: list[str], words: list[str]) -> None:
    for new_word in new_words:
        words.append(new_word.strip())
    
    
def remove_word(word: str, words: list[str]) -> None:
    if word in words:
        words.remove(word)

def main():
    words = get_words_list()
    new_words = input("quais as palavras? ").split(",")
    add_new_words(new_words, words)
    
    print_words(words)
    update_words_file(words)

if __name__ == "__main__":
    main()