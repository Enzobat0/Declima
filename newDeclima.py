import Word_rearrangement
import riddle

def display_instructions():
    print("Welcome to DECLIMA!")
    print("DECLIMA is a game where you can have fun while learning more about climate change.")
    print("You can choose between two games:")
    print("1. Word Game: Rearrange letters to find a word related to climate change.")
    print("2. Riddle Game: Answer tricky questions related to climate change.")
    print()

def get_user_choice():
    while True:
        choice = input("If you want to play the Word Game, press 1. If you want to play the Riddle Game, press 2: ")
        if choice in ('1', '2'):
            return choice
        else:
            print("Incorrect input. Please choose either 1 or 2.")

def main():
    display_instructions()
    choice = get_user_choice()

    if choice == '1':
        Word_rearrangement.game()
    elif choice == '2':
        riddle.start_game()

if __name__ == '__main__':
    main()
