from scripts.Proj1_HangmanGame.t5_class import Game as game

random_word = game.Word_Generation()
random_word.pop(-1)
random_word_constant = list(random_word)


guessed_letters = ['_' for _ in range(len(random_word))]
guessed_letters_sorted = []
letter = ''

tries = int(input('Enter the number of attempts for which you want to guess one letter(max - 13, min - 1): '))
if tries < 1 or tries > 13:
    print('InvalidValue: the number of tries should be - 13 >= number of attempts >= 1 ')
    raise SystemExit

while True:
    guessed_letters_sorted = game.Print_Guessed_Letters_Sorted(guessed_letters_sorted, letter)
    game.Print_Guessed_Letters(guessed_letters)
    letter = input('\n\nEnter the letter: ')
    if len(letter) != 1 or isinstance(letter, str) == False:
        print('InvalidValueException')
        break
    tries = game.Check_Tries(tries, letter, random_word)

    if letter in random_word:
        guessed_letters[random_word.index(letter)] = letter
        random_word[random_word.index(letter)] = '_'

    if game.Won_Or_Lost(tries, random_word_constant, guessed_letters) == 1:
        break
