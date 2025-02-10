import random

def display_list(list):
    """imprime todos os caracteres de uma lista separados por espaços no console"""
    for char in list:
        print(char, end=" ")
    print()
    
    
def display_lives(guesses):
    """imprime a quantidade de vidas restantes no console"""
    print(f"you have {guesses} guesses left!")
    

def compare_guess(secret_word, hint, guess):
    """compara o chute com a palavra secreta, atualizando as letras acertadas"""
    correct_guess = False
    for i in range(len(secret_word)):
            if secret_word[i] == guess:
                hint[i] = guess
                correct_guess = True
    return correct_guess


def check_guess(guess, hint, secret_word, guessed_letters):
    """verifica o chute do usuário"""
    if len(guess) > 1:
        if len(guess) != len(secret_word):   
            return False, False
        if secret_word == list(guess):
            return True, True
        print(secret_word, guess)
        return False, False

    if guess not in guessed_letters:
        guessed_letters.add(guess)
        return compare_guess(secret_word, hint, guess), secret_word == hint
        
    print("you already guessed this letter! try again.")
    return True, False


def main():
    """executa o código principal para o jogo"""
    words = ("phone", "internet", "python")

    secret_word = list(random.choice(words))
    hint = ["_" for x in secret_word]
    guessed_letters = set()

    has_won = False
    guesses = 3

    while not has_won and guesses > 0:
        display_lives(guesses)
        display_list(hint)
        guess = input("what is your guess? ").lower()
        correct_guess, has_won = check_guess(guess, hint, secret_word, guessed_letters)
        if not correct_guess:
            guesses -= 1
            
    if not has_won:
        print("you lost, better luck next time")
        return
    
    display_list(secret_word)
    print(f"congrats! you won!")
        
        
if __name__ == "__main__":
    main()