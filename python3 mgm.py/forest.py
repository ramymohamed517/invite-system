
import time
import random

print("Welcome to the Scary Forest Game!")
print("You are now inside a scary forest full of monsters and darkness.")

player_name = input("What's your name, brave adventurer? ")
print(f"{player_name}, your adventure begins now... Good luck!")

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.7)
    print()

def ask_choice():
    
    while True:
        choice = input("Choose (1 / 2 / 3 / 4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Wrong choice. Try again.")

def random_event():
    events = [
        "You hear a sound...",
        "Something moved!",
        "Wind is blowing...",
        "It's too quiet..."
    ]
    return random.choice(events)

def one_round(score):
   
    print("What do you want to do?")
    print("1. Look around")
    print("2. Run away")
    print("3. Climb a tree")
    print("4. Rest")

    choice = ask_choice()

    if choice == "1":
        slow_print(random_event())
        score += random.randint(1, 3)

    elif choice == "2":
        if random.random() < 0.3:
            slow_print("You escaped!")
            return score, True
        else:
            slow_print("You failed to escape.")
            score -= 2

    elif choice == "3":
        if random.random() < 0.5:
            slow_print("You saw something helpful.")
            score += 2
        else:
            slow_print("You slipped!")
            score -= 2

    elif choice == "4":
        if random.random() < 0.5:
            slow_print("You feel better now.")
            score += 1
        else:
            slow_print("You feel nervous...")
            score -= 1

    return score, False

def start_game():
    slow_print("Try to survive or escape.")

    score = 10
    turns = 0

    while score > 0 and turns < 5:
        score, escaped = one_round(score)
        if escaped:
            print("You Win!")
            break
        print("Score:", score)
        turns += 1
    else:
        if score <= 0:
            print("You lost...")
        elif score >= 15:
            print("You survived the forest!")
        else:
            print("Game over.")

    again = input("Play again? (yes/no): ").lower()
    if again == "yes":
        start_game()
    else:
        print("Thanks for playing! Goodbye!")

def main():
    start_game()

if __name__ == "__main__":
    main()