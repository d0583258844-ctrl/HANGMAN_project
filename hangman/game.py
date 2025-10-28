def init_state(secret: str, max_tries: int= 6 ) -> dict:
    
    return {
        "secret": secret,
        "display":  ["_" for _ in secret],
        "guessed": set(),
        "wrong_guesses": 0,
        "max_tries":max_tries
        }

 
 


def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) != 1:
        return False,"Enter a single letter!."
    elif not ch.isalpha():
            return False,"Enter a letter only, not a number or symbol!"
    elif ch in guessed:
                return False, "The letter has already been typed. choich another one"        
    else:
        return True,"greate choich!"






def apply_guess(state: dict, ch: str) -> bool:
    print(state["secret"])
    ch = ch.lower()
    state["guessed"].add(ch)    # print(state["guessed"])
    if ch in state["secret"]:
        for i in range(len(state["secret"])):
            print(state["secret"][i])
            if state["secret"][i] == ch:
                state["display"][i] = ch
        return True
    state["wrong_guesses"] += 1
    return False 
    
    
    
            
        


def is_won(state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    else:
        return False
      



def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True, "you lose, the game is over."
    else:
        return False


     


def render_display(state: dict) -> str:
    return "this is your corect gusses", state["display"]



def render_summary(state: dict) -> str:
    return "That's the word you had to find:",state["secret"], \
    "These are the letters you entered:",state["guessed"]











# def apply_guess(state: dict, ch: str) -> bool:
    # validation_tuple = validate_guess(ch, state["guessed"])
    # if validation_tuple[0]:
    #     state["guessed"].add(ch)
    #     if ch in state[]
    # return





# if __name__ == "__main__":
#     chosen_word = choose_secret_word(WORDS)
#     state = init_state(chosen_word,max_tries=5)
#     print(f"state init: {state}")

#     print(validate_guess("d",state["guessed"]))
    
#     print(f"wrong_guesses:",state["wrong_guesses"])
#     apply = apply_guess(state, "l")
    
#     wining = is_won(state)
#     print(wining)

#     lost = is_lost(state)
#     print(lost)

#     print(render_display(state))


#     print(render_summary(state))