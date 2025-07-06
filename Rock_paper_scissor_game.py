import random
import os

# Optional: Colored output
try:
    from colorama import init, Fore, Style
    init()
except ImportError:
    Fore = Style = type('', (), {'RESET_ALL': '', 'GREEN': '', 'RED': '', 'CYAN': '', 'YELLOW': ''})()

choices = ['rock', 'paper', 'scissors']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def decide_winner(player, computer):
    if player == computer:
        return 'draw'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'player'
    else:
        return 'computer'

def play_game():
    player_score = 0
    computer_score = 0
    round_num = 1

    print(f"{Fore.GREEN}Welcome to Rock, Paper, Scissors!{Style.RESET_ALL}")
    print("Enter R for Rock, P for Paper, S for Scissors, or E to Exit.\n")

    while True:
        print(f"{Fore.YELLOW}--- Round {round_num} ---{Style.RESET_ALL}")
        user_input = input("Your choice (R/P/S or E to exit): ").strip().lower()

        if user_input == 'e':
            print(f"{Fore.CYAN}Thanks for playing! Final score: You {player_score} - {computer_score} Computer{Style.RESET_ALL}")
            break

        mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        if user_input not in mapping:
            print(f"{Fore.RED}Invalid choice! Please enter R, P, S, or E.{Style.RESET_ALL}")
            continue

        player_choice = mapping[user_input]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {Fore.CYAN}{player_choice.capitalize()}{Style.RESET_ALL}")
        print(f"Computer chose: {Fore.MAGENTA}{computer_choice.capitalize()}{Style.RESET_ALL}")

        winner = decide_winner(player_choice, computer_choice)

        if winner == 'player':
            print(f"{Fore.GREEN}You win this round! 🎉{Style.RESET_ALL}")
            player_score += 1
        elif winner == 'computer':
            print(f"{Fore.RED}Computer wins this round! 🤖{Style.RESET_ALL}")
            computer_score += 1
        else:
            print(f"{Fore.YELLOW}It's a draw! 🤝{Style.RESET_ALL}")

        print(f"Score: You {player_score} - {computer_score} Computer\n")
        round_num += 1

if __name__ == "__main__":
    play_game()
