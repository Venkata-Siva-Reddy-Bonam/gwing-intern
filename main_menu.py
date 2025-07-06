import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def run_game(file_name):
    print(f"\nRunning {file_name}...\n")
    time.sleep(1)
    os.system(f"python \"{file_name}\"")

def main():
    games = {
        "1": ("Adventure Game", "adventure_game.py"),
        "2": ("Number Guessing Game", "Number_guessing_game.py"),
        "3": ("Quiz Game", "Quiz_game.py"),
        "4": ("Rock Paper Scissor Game", "Rock_paper_scissor_game.py"),
        "5": ("Exit", None)
    }

    while True:
        clear_screen()
        print("🎮 Welcome to the Ging Intern Game Hub 🎮\n")
        for key, (title, _) in games.items():
            print(f"{key}. {title}")
        
        choice = input("\nChoose a game to play (1-5): ").strip()

        if choice in games:
            if choice == "5":
                print("Goodbye! 👋")
                break
            else:
                _, filename = games[choice]
                run_game(filename)
                input("\nPress Enter to return to menu...")
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
