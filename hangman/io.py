from hangman.game import is_won, render_display

def prompt_guess() -> str:
    your_letter = input("enter a CH, NOT number or sign! :")
    return your_letter
# print(prompt_guess())



def print_status(state: dict) -> None:
    render_display(state)
    print(state["guessed"])
    print(f"your's left guesses:",state["max_tries"] - state["wrong_guesses"], state["secret"], state["max_tries"])




def print_result(state: dict) -> None:
    temp = is_won(state)
    if temp:
        print("you win, cangraguletions!")
    else:
        print("you lose, you passed the guesses num")







# if __name__ == "__main__":
    # chosen_word = choose_secret_word(WORDS)
# state = init_state(chosen_word,max_tries=5)
# print(f"state init: {state}")
# render_display(state)

# your_input = prompt_guess()
# print(your_input)

# validate_guess(your_input,state["guessed"])
# apply_guess(state,your_input)
# _status = print_status(state)
# print(_status)

# ending = print_result(state)
# print(ending)