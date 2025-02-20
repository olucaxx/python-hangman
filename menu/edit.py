import menu.interface as interface
from utils.helpers import clear_terminal
import data.words as words


def edit_loop():        
    clear_terminal()
    interface.display_edit_menu()
    
    while True:
        edit_menu_option = interface.get_menu_option_from_user()
        match edit_menu_option.strip():
            case "1":
                interface.display_words(words.get_words_from_file())
                clear_terminal()
                interface.display_edit_menu()
            case "2":
                words.add_new_words(interface.get_words_to_add())
                clear_terminal()
                interface.display_edit_menu()
            case "3":
                words.remove_words(interface.get_words_to_remove())    
                clear_terminal()
                interface.display_edit_menu()
            case "4":
                break
            case _:
                interface.show_invalid_option_warning()