from menu.edit import edit_loop
from menu.game import game_loop
from utils.helpers import clear_terminal
from menu.interface import show_invalid_option_warning

def print_menu() -> None:
        print("1. Jogar \n2. Editar Palavras \n3. Sair")


def main():
    clear_terminal()
    print_menu()
    
    while True:
        main_menu_option = input("Digite o número da opção desejada: ")
        match main_menu_option.strip():
            case "1":
                game_loop()
                clear_terminal()
                print_menu()
                
            case "2":
                edit_loop()
                clear_terminal()
                print_menu()
                    
            case "3":
                print("\nEncerrando...")
                exit()
                
            case _:
                show_invalid_option_warning()
                
        
if __name__ == "__main__":
    main()