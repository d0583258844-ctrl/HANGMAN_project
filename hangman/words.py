import random
def choose_secret_word(words: list[str]) -> str:
    word = random.choice(words)
    return word
    

# print(choose_secret_word(WORDS))

# if __name__ == "__main__":
#    secret = choose_secret_word(WORDS)
#    print(secret)