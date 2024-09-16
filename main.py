# HANGMAN GAME

"""Design a text-based Hangman game. The program selects a random word, 
   and the player guesses one letter at a time to uncover the word. 
   You can set a limit on the number of incorrect guesses allowed."""

import random

def gen_word():
    # Generate the random word
    with open("file.txt") as f:
        file_content = f.readlines()
    
    content = random.choice(file_content).strip()
    content = content.lower()
    # print(content)
    return content

def char_check(char, content):
    # Check each character if it's in the word
    if(char in content):
        print(f"Yes, '{char}' is in the word.")
    else:
        print(f"No, '{char}' is not in the word.")
        
def check_word(word, content):
    # Match the guessed word from the actual word 
    if (word == content):
        print(f"\nYou won, \nWord '{word}' is correct.")
    else:
        print(f"\nYou Lose, \nCorrect word is {content}.")
    pass


def hangman():
    # Main function
    print("\n!!! Word Guessing Game !!!\n")
    content = gen_word()
    word_len = len(content)
    symbol = '_ ' * (word_len-1)
    print(f"Word: {content[0]} {symbol}")
    
    # Main game loop
    i = 0
    while(i!=word_len):

        char = input("Guess the Letter: ").lower()
        char_check(char, content)
        print(f"You have {(word_len-1)-i} chances left.")
        print("")
        i+=1

    word = input("Guess the word: ")
    check_word(word, content)

if __name__ == "__main__":
    hangman()