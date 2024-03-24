import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    #The loop will continue to run as long as the guessed variable is False and the number of tries is greater than 0. If guessed becomes True (the player guesses the correct word or the word has been guessed ), or the number of incorrect guesses (tries) drops to 0 (the player runs out of incorrect guesses), the loop will stop.
    while not guessed and tries > 0:
        #The player will enter a letter or word to guess. The upper() function is used to ensure that all input characters are converted to upper case to accommodate future comparisons.
        guess = input("Please guess a letter or word: ").upper()
        #Checks whether the player has entered a character and whether that character is a letter or not.
        if len(guess) == 1 and guess.isalpha():
            #Check if the letter has been guessed before. If it has been guessed, an error message is reported and the player is asked to re-enter.
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                #If the letter does not appear in the word to be guessed, reduce the number of incorrect guesses (tries) by 1 and add the letter to the guessed_letters list to prevent the player from guessing that letter again.
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                #If the character appears in the word to be guessed, notify success and update the status of the guessed word (word_completion) by replacing the _ characters corresponding to the position of the correctly guessed character.
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        #If the word does not match the word to be guessed, reduce the number of incorrect guesses (tries) by 1 and add the word to the guessed_words list to prevent players from guessing the word again.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        #If the word matches the word to be guessed, notify success and update the status of the guessed word (word_completion) with the word to be guessed.
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else: #If the player does not enter a valid character or word, report an error and ask to re-enter.
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

                """
                   --------
                   |      |C
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()