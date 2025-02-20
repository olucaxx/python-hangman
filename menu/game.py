from utils.helpers import clear_terminal
from game.engine import execute_game
import menu.interface as interface

def game_loop():
    clear_terminal()
    execute_game()
    
    while True:
        play_again = interface.ask_to_play_again()
        match play_again:
            case "sim":
                clear_terminal()
                execute_game()
            case "nao":
                break
            case _:
                interface.show_invalid_option_warning()
                