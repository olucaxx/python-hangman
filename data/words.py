from random import choice

FILE = "data/wordslist.txt"

def get_words_from_file() -> list[str]:
    with open(FILE) as file:
        return [line.strip() for line in file]


def update_words_file(words: list[str]) -> None:
     with open(FILE, "w") as file:
         for word in words:
            file.write(f"{word}\n")


def select_random_word() -> str:
    """seleciona uma palavra aleatória do arquivo words.txt e retorna ela"""
    return choice(get_words_from_file())
    

def add_new_words(new_words: list[str]) -> None:
    words = get_words_from_file()
    
    for new_word in new_words:
        if new_word.strip() != "":
            words.append(new_word.strip())
    
    update_words_file(words)
    
    
def remove_words(removed_words: list[str]) -> None:
    words = get_words_from_file()
    for removed_word in removed_words:
        if removed_word.strip() in words:
            words.remove(removed_word.strip())
            
    update_words_file(words)
        