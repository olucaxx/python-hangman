def display_introduction() -> None:
    print("Você pode tentar chutar uma letra por vez ou arriscar a palavra inteira! Ao errar irá perder uma chance.")

def display_hint(char_list: list) -> None:
    """imprime todos os caracteres de uma lista separados por espaços no console"""
    for char in char_list:
        print(char, end=" ")
    print()
    
    
def display_lives(guesses: int) -> None:
    """imprime a quantidade de vidas restantes no console"""
    print(f"\nvocê tem {guesses} tentativas")
    
    
def get_user_guess() -> str:
    return input("qual o seu chute? ").lower().strip()


def show_repetead_letter_warning() -> None:
    print("você já tentou essa letra, tente outra!")
    
    
def show_defeat_message(secret_word) -> None:
    print("\nvocê perdeu")
    print(f"a palavra era \"{secret_word}\"")
    
    
def show_victory_message(secret_word) -> None:
    print(f"\nparabéns! você acertou!")
    print(f"a palavra era \"{secret_word}\"")