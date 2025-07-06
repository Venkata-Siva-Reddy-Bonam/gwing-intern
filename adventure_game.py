import time
import os

try:
    from colorama import init, Fore, Style
    init()
except ImportError:
    Fore = Style = type('', (), {'RESET_ALL': '', 'GREEN': '', 'RED': '', 'CYAN': '', 'YELLOW': ''})()

def slow_print(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def intro():
    clear_screen()
    slow_print(f"{Fore.GREEN}Welcome to the Forest of Fate!{Style.RESET_ALL}")
    slow_print("You find yourself at the edge of a mysterious forest...")
    slow_print("Legends say that within the forest lies treasure, danger, and secrets.")
    slow_print("Do you dare to enter?\n")
    input("Press Enter to begin your adventure...")

def choose_path():
    slow_print("\nTwo paths lie ahead:")
    slow_print("1. A dark, twisted trail covered in fog.")
    slow_print("2. A sunny, flower-lined road that seems safe.\n")
    while True:
        choice = input(f"{Fore.YELLOW}Which path do you take? (1 or 2): {Style.RESET_ALL}").strip()
        if choice in ['1', '2']:
            return choice
        else:
            print(f"{Fore.RED}Invalid input. Choose 1 or 2.{Style.RESET_ALL}")

def dark_path():
    slow_print(f"\n{Fore.CYAN}You walk cautiously into the dark path...{Style.RESET_ALL}")
    slow_print("The trees close in around you. You hear a growl.")
    slow_print("A wild wolf appears!\n")
    slow_print("1. Fight the wolf.")
    slow_print("2. Try to run away.\n")

    while True:
        action = input(f"{Fore.YELLOW}What do you do? (1 or 2): {Style.RESET_ALL}").strip()
        if action == '1':
            slow_print(f"\n{Fore.GREEN}You bravely fight the wolf and scare it away! 🐺{Style.RESET_ALL}")
            treasure_ending()
            break
        elif action == '2':
            slow_print(f"\n{Fore.RED}You trip while running... The wolf catches you. Game Over! 💀{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Choose 1 or 2 only!{Style.RESET_ALL}")

def sunny_path():
    slow_print(f"\n{Fore.CYAN}You stroll down the sunny path, enjoying the scenery.{Style.RESET_ALL}")
    slow_print("You find a glowing well that whispers your name.\n")
    slow_print("1. Drink from the well.")
    slow_print("2. Walk away cautiously.\n")

    while True:
        action = input(f"{Fore.YELLOW}Your choice? (1 or 2): {Style.RESET_ALL}").strip()
        if action == '1':
            slow_print(f"\n{Fore.RED}You drink... and transform into a tree. Forever part of the forest! 🌳{Style.RESET_ALL}")
            break
        elif action == '2':
            slow_print(f"\n{Fore.GREEN}You resist the temptation and discover a hidden map behind the well! 🗺️{Style.RESET_ALL}")
            treasure_ending()
            break
        else:
            print(f"{Fore.RED}Choose 1 or 2 only!{Style.RESET_ALL}")

def treasure_ending():
    slow_print(f"\n{Fore.MAGENTA}Following the clues, you find a hidden cave behind a waterfall...{Style.RESET_ALL}")
    slow_print("Inside lies the legendary treasure of the forest! 💰🏆")
    slow_print(f"{Fore.GREEN}You are now the richest adventurer in the land! 🎉{Style.RESET_ALL}")

def main():
    intro()
    path = choose_path()
    if path == '1':
        dark_path()
    else:
        sunny_path()

    slow_print(f"\n{Fore.CYAN}Thanks for playing The Forest of Fate!{Style.RESET_ALL}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
