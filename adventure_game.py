import time
import random

creature = ["wicked witch", "gorgon", "troll", "giant spider"]

def pause_print(message):
    time.sleep(1)
    print(message)

def intro():
    global threat
    threat = random.choice(creature)
    
    pause_print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    pause_print("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")

    while True:
        pause_print("Enter 1 to knock on the door of the house.")
        pause_print("Enter 2 to peer into the cave.")
        pause_print("What would you like to do?")
        pause_print("(Please enter 1 or 2).")
        choice = input()
        if choice == '1':
            house()
            break
            
        elif choice == '2':
            cave()
            break

        else:
            pause_print("Invalid choice, please try again.")
            continue

    restart()

def house():
    pause_print("You approach the door of the house.")
    pause_print(f"You are about to knock when the door opens and out comes a {threat}!")
    pause_print(f"Eep! The {threat} has attacked you!")
    pause_print("You have been defeated!")

def cave():
    pause_print("You peer into the cave.")
    pause_print("It's dark and spooky, but you find a shiny sword!")
    pause_print("You take the sword and feel more confident.")
    pause_print("You approach the door of the house.")
    pause_print(f"You are about to knock when the door opens and out steps a {threat}!")
    pause_print(f"You bravely draw your sword to face the {threat}!")
    pause_print(f"After a fierce battle, you have defeated the {threat}!")
    pause_print("You have saved the village!")

def restart():
    while True:
        pause_print("Would you like to play again? (y/n)")
        choice = input()
        if choice == 'y':
            intro()
            return
        
        elif choice == 'n':
            pause_print("Thanks for playing! Goodbye.")
            return
         
        else:
            pause_print("Invalid choice, please try again.")
            continue
    
intro()