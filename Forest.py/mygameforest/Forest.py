import random

print("Welcome to the Scary Forest Game!")
print("You are now inside a scary forest. There are many monsters, and darkness covers the place. Terrifying sounds can be heard.")
name = input("What's your name? ")
treasure_spot = 0
health = 100
exit_flag = False  # Changed from 'exit' which is a built-in function

def forest_game():
    global health  # Need to declare health as global to modify it inside function
    
    print("\n1. Take the shadowy trail between the twisted trees")
    print("2. Follow the strange sound coming from the right")
    choice = input("Choose (1-2): ")
    
    event = random.choice(["monster", "treasure", "friend", "nothing"])
    
    if choice == "1":  # Input is string by default, so compare with string
        print("\nYou chose to take the shadowy trail between the twisted trees")
        if event == "monster":
            print("A fire monster appears!")
            health -= 30
        elif event == "treasure":  # Changed from 'if event == 1' which was wrong
            print("You found a hidden treasure chest under the leaves!")
            treasure_spot += 1
        elif event == "friend":
            print("A friendly forest spirit heals you!")
            health += 20
        else:
            print("You walk safely through the dark path.")
    
    elif choice == "2":
        print("\nYou follow the strange sound...")
        # Add similar event handling for choice 2 here
    
    print(f"\nYour health is now: {health}")
