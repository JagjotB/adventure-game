import time
import random

creature = ["wicked witch", "gorgon", "troll", "giant spider"]

def pause_print(message):
    time.sleep(1)
    print(message)

pause_print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
pause_print("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")

def intro():
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
            intro()

def house():
    threat = random.choice(creature)
    pause_print("You approach the door of the house.")
    pause_print(f"You are about to knock when the door opens and out comes a {threat}!")
    pause_print(f"Eep! The {threat} has attacked youo!")
    pause_print("You have been defeated!")
    pause_print("Would you like to play again? (y/n)")
    

def cave():
    pause_print("You peer into the cave.")
    pause_print("It's dark and spooky, but you find a shiny sword!")
    pause_print("You take the sword and feel more confident.")
    pause_print("You approach the door of the house.")
    pause_print("You are about to knock when the door opens and out steps a wicked witch!")
    pause_print("You bravely draw your sword to face the wicked witch!")
    pause_print("After a fierce battle, you have defeated the wicked witch!")
    pause_print("You have saved the village!")
    pause_print("Would you like to play again? (y/n)")
    
intro()