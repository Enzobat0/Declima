import Word_rearrangement
import riddle

def display_instructions():
    # ... (same as in the new code)

def get_user_choice():
    # ... (same as in the new code)

def main():
    display_instructions()
    choice = get_user_choice()

    if choice == '1':
        Word_rearrangement.game()
    elif choice == '2':
        riddle.start_game()

if __name__ == '__main__':
    main()


