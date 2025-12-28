import time

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
            pause_print("You approach the door of the house.")
        elif choice == '2':
            pause_print("You peer into the cave.")
        else:
            pause_print("Invalid choice, please try again.")
            intro()

intro()