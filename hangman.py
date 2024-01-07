import random
from words import words_list



def get_valid_word():
    word = random.choice(words_list)
    #to get a valid word because the words array has - and blanks
    while '-' in word or '' in word:
        word = random.choice(words_list)

    return word.upper()


def hangman(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play hangman!")
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input('Guess a letter or a word: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Ýou already guessed the letter.', guess)
            elif guess not in word:
                print(guess, 'not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Good job {guess} is in the word.')
                guessed_letters.append(guess)
                words_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    words_as_list[index] = guess
                word_completion = "".join(words_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word. ', guess)
            elif guess != word:
                print(guess, ' is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Invalid character. Try again.')

    if guessed:
        print('Congrats!, You  guessed the word.')
    else:
        print(f'Sorry! {word} is the correct word.')


def main():
    word = get_valid_word()
    hangman(word)
    while input('Play again?? (Y/N)').upper() == 'Y':
        word = get_valid_word()
        hangman(word)


if __name__ == "__main__":
    main()

