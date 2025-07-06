import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number (1–100): "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"You got it in {attempts} tries!")
            break

if __name__ == "__main__":
    guess_number()
