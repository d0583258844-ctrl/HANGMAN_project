from hangman.game import *
from hangman.io import *
from hangman.words import *
from hangman.data.data import WORDS

def main():
    secret = choose_secret_word(WORDS)
    state = init_state(secret,6)

    while not is_won(state) and not is_lost(state):
        print_status(state)
        print(render_display(state))
        _input = prompt_guess()
        x = validate_guess(_input, state["guessed"])
        if x[0]==False:
            continue
        _ = apply_guess(state, _input)
    print_result(state)




    












    # state = init_state(secret)
    # while not is_won(state):
    #     user_guess = prompt_guess()
    #     apply_guess(state,user_guess)
    #     validate_guess(state,guessed= prompt_guess)

# words = play(choose_secret_word(WORDS), max_tries=6)


if __name__ == "__main__":
    main()