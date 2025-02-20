def show_invalid_option_warning() -> None:
    print("Opção inválida!")
    

def ask_to_play_again() -> str:
    return input("\nGostaria de jogar novamente? sim/nao\n").strip().lower().replace("ã", "a")


def get_words_to_add() -> str:
    print("\nCaso deseje mais de uma palavra, separe por vírgula: exemplo1, exemplo2, exemplo3")
    return input("Gostaria de adicionar qual(is) palavra(s) na lista?\n").split(",")


def get_words_to_remove() -> str:
    print("\nCaso deseje mais de uma palavra, separe por vírgula: exemplo1, exemplo2, exemplo3")
    return input("Gostaria de remover qual(is) palavra(s) da lista?\n").split(",")


def get_menu_option_from_user() -> str:
    return input("Digite o número da opção desejada: ").strip()


def display_words(words) -> None:
    print("\nListando as palavras: ")
    if len(words) == 0:
        print("Nenhuma palavra encontrada, adicione alguma!\n")
        return
    
    for index, word in enumerate(words, start=1):
        print(f"{index}. '{word}'")
    input("\nDigite qualquer tecla para continuar. ")
    
    
def display_edit_menu() -> None:
    print("1. Listar palavras \n2. Adicionar palavras \n3. Remover palavras \n4. Voltar")  