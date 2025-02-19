from hangman import execute_game
import manage_words as words
from os import system as os_system
from platform import system as platform_system

def clear_terminal():
    os_system("cls" if platform_system() == "Windows" else "clear")
    
def game_loop():
    clear_terminal()
    
    execute_game()
    
    play_again = True
    while(play_again):
        play_again = input("\nGostaria de jogar novamente? sim/nao\n")
        match play_again.strip().lower().replace("ã", "a"):
            case "sim":
                clear_terminal()
                execute_game()
            case "nao":
                play_again = False
            case _:
                print("Opção inválida, digite 'sim' ou 'nao'!")


def edit_loop():
    instrucao = "\nCaso deseje mais de uma palavra, separe por vírgula: exemplo1, exemplo2, exemplo3"
    words_list = words.get_words_list()
    
    def print_menu():
        print("1. Listar palavras \n2. Adicionar palavras \n3. Remover palavras \n4. Voltar")  
        
        
    def remove_words():
        print(instrucao)
        input_words = input("Gostaria de remover qual(is) palavra(s) da lista?\n").split(",")
        words.remove_words(input_words, words_list)
        words.update_words_file(words_list)
        
       
    def add_words():
        print(instrucao)
        input_words = input("Gostaria de adicionar qual(is) palavra(s) na lista?\n").split(",")
        words.add_new_words(input_words, words_list)
        words.update_words_file(words_list)
        
        
    def list_words():
        words.print_words(words_list)
        input("Digite qualquer tecla para continuar. ")
        
    editing = True
    while editing:
        clear_terminal()
        print_menu()
        edit_menu_option = input("Digite o número da opção desejada: ")
        match edit_menu_option.strip():
            case "1":
                list_words()
            case "2":
                add_words()
                
            case "3":
                remove_words()     
                       
            case "4":
                editing = False
                break
            
            case _:
                print("Opção inválida.")


def main():
    def print_menu():
        print("1. Jogar \n2. Editar Palavras \n3. Sair")
    
    while(True):
        clear_terminal()
        print_menu()
        main_menu_option = input("Digite o número da opção desejada: ")
        match main_menu_option.strip():
            case "1":
                game_loop()
                
            case "2":
                edit_loop()
                    
            case "3":
                print("Encerrando...")
                exit()
                
            case _:
                print("Opção inválida.")
                
        
if __name__ == "__main__":
    main()