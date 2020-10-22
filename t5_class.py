import random
import os


class Game:
    @staticmethod
    def Word_Generation():
        print('...**Generating random word**...\n')
        print('**Random word was generated**\n...**Starting the game**...\n**Game started, good luck!**')
        with open(f'{os.getcwd()}\\Game-Guess-the-word\\WordsStockRus.txt', 'r', encoding='UTF-8') as file:
            file = list(file)
            random_word = list(random.choice(file))
        return random_word

    @staticmethod
    def Won_Or_Lost(tries: int, random_word: list, guessed_letters: list):
        if tries == 0:
            print(f'Sorry bro, you lost(\nThe hidden wor was - {str(random_word)}\nTry again if you want to win\n')
            return 1

        elif random_word == guessed_letters:
            print('\n\n*--->C-O-N-G-R-A-T-U-L-A-T-I-O-N-S-!-!<---*\nY=O=U W=O=N=!\n')
            return 1

    @staticmethod
    def Check_Tries(tries: int, letter: str, random_word: int):
        if letter in random_word:
            tries += 1
            print(f'You guessed the letter! You have {tries} tries')
        else:
            tries -= 1
            print(f'Wrong letter, you have only {tries} attempts left! Be careful')
        return tries

    @staticmethod
    def Print_Guessed_Letters(guessed_letters: list):
        print('\n\nYour guessed letters: ')
        for i in range(len(guessed_letters)):
            print(guessed_letters[i], end=' ')

    @staticmethod
    def Print_Guessed_Letters_Sorted(guessed_letters_sorted: list, letter: str):
        guessed_letters_sorted.append(letter)
        print('\nLetters you entered: ')
        for i in range(len(guessed_letters_sorted)):
            print(guessed_letters_sorted[i], end=' ')
        return sorted(guessed_letters_sorted)
