import game.interface as interface
from data.words import select_random_word

from typing import Tuple

def compare_guess_with_hint(secret_word: str, hint: str, guess: str) -> bool:
    """compara o chute com a palavra secreta, atualizando as letras acertadas"""
    correct_guess = False
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            hint[i] = guess
            correct_guess = True
    return correct_guess


def validate_guess(guess: str, hint: list, secret_word: str, guessed_letters: set) -> Tuple[bool, bool]:
    """verifica o chute do usuário"""
    if len(guess) > 1:
        if len(guess) != len(secret_word):   
            return False, False
        if secret_word == guess:
            hint[:] = list(secret_word)
            return True, True
        return False, False

    if guess not in guessed_letters:
        guessed_letters.add(guess)
        correct_guess = compare_guess_with_hint(secret_word, hint, guess)
        return correct_guess, hint == list(secret_word)
    
    interface.show_repeated_letter_warning()
    return True, False


def execute_game() -> None:
    """executa o código principal para o jogo"""
    secret_word = select_random_word()
    hint = ["_" for x in secret_word]
    guessed_letters = set()
    
    has_won = False
    guesses = 3

    interface.display_introduction()
    
    while not has_won and guesses > 0:
        interface.display_lives(guesses)
        interface.display_hint(hint)
        guess = interface.get_user_guess()
        correct_guess, has_won = validate_guess(guess, hint, secret_word, guessed_letters)
        if not correct_guess:
            guesses -= 1
            
    if not has_won:
        interface.show_defeat_message(secret_word)
        return

    interface.show_victory_message(secret_word)
