import os

# Optional: Color support
try:
    from colorama import init, Fore, Style
    init()
except ImportError:
    Fore = Style = type('', (), {'RESET_ALL': '', 'GREEN': '', 'RED': '', 'CYAN': '', 'YELLOW': ''})()

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer.upper()

    def display(self):
        print(f"{Fore.CYAN}{self.prompt}{Style.RESET_ALL}")
        for i, option in enumerate(self.options, start=65):  # A=65
            print(f"  {chr(i)}. {option}")
        print(f"\n{Fore.YELLOW}Enter A/B/C/D to answer, S to skip, or E to exit.{Style.RESET_ALL}")

    def check_answer(self, user_input):
        return user_input == self.answer

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def run_quiz(questions):
    score = 0
    total = len(questions)
    current = 0

    clear_screen()
    print(f"{'='*40}\n{Fore.GREEN}       Welcome to the Quiz Game!{Style.RESET_ALL}\n{'='*40}\n")

    while current < total:
        q = questions[current]
        print(f"\nQuestion {current + 1}/{total}")
        q.display()
        user_input = input(f"{Fore.YELLOW}Your choice: {Style.RESET_ALL}").strip().upper()

        if user_input in ['A', 'B', 'C', 'D']:
            if q.check_answer(user_input):
                print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                score += 1
            else:
                print(f"{Fore.RED}Wrong! The correct answer was {q.answer}.{Style.RESET_ALL}")
            current += 1
        elif user_input == 'S':
            print("Skipping this question.")
            current += 1
        elif user_input == 'E':
            print(f"{Fore.RED}Exiting the quiz early...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid input! Please choose A/B/C/D/S/E.{Style.RESET_ALL}")
        print("-" * 40)

    print(f"\n{Fore.CYAN}Quiz Completed! 🎉{Style.RESET_ALL}")
    print(f"Your Final Score: {score}/{total}  ({(score/total)*100:.1f}%)")

# Sample Questions
quiz_questions = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "C"),
    Question("Which language is used for web development?", ["Python", "Java", "HTML", "C++"], "C"),
    Question("What is 5 + 7?", ["10", "12", "11", "13"], "B"),
    Question("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], "C")
]

if __name__ == "__main__":
    run_quiz(quiz_questions)
