def get_words_list() -> list[str]:
    with open("words.txt") as file:
        return [line.strip() for line in file]


def update_words_file(words: list[str]) -> None:
     with open("words.txt", "w") as file:
         for word in words:
            file.write(f"{word}\n")


def print_words(words: list[str]) -> None:
    print("\nListando as palavras: ")
    if len(words) == 0:
        print("Nenhuma palavra encontrada, adicione alguma!\n")
        return
    
    for index, word in enumerate(words, start=1):
        print(f"{index}. '{word}'")
    print()
    

def add_new_words(new_words: list[str], words: list[str]) -> None:
    print(new_words)
    input("digitarrr")
    for new_word in new_words:
        if new_word.strip() != "":
            words.append(new_word.strip())
        print(True)
    
    
def remove_words(removed_words: list[str], words: list[str]) -> None:
    for removed_word in removed_words:
        if removed_word.strip() in words:
            words.remove(removed_word.strip())
        