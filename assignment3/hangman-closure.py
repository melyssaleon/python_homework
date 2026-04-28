# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for ch in secret_word:
            if ch in guesses:
                display += ch
            else:
                display += "_"
        print(display)
        return set(secret_word).issubset(set(guesses))
    return hangman_closure


if __name__ == "__main__":
    word = input("Enter secret word: ")
    game = make_hangman(word)
    finished = False
    while not finished:
        guess = input("Guess a letter: ")
        finished = game(guess)
    print("You won!")