# Create a list of words, we pick one random word, we ask the user to guess that word
# input, random, time to delay

#GAME RULES: shows the user the list of words depending on level of difficulty chosen, gives the user 5 tries to guess the word and the user can input one letter or multiple letters,
#each time the user attempts to guess the turns will decrease until they guess correctly

import random
import time

#retrieves the words from a file
def game_data(levelOfDifficulty):
    file1 = open("RandomFile.txt","r")
    lines = file1.readlines()
    #returns a list of words
    #each line in the file is considered an element (1st line is 0 index, etc.)
    return(lines[levelOfDifficulty-1].strip().split(","))

def game():
    # ask user for information
    name = input("What is your name? ")

    # create a list of words
    # pick a random word
    # the user to guess
    print(name,end=', ')
    game = input("do you want to play? ")

    while game == 'yes':
        levelOfDifficulty = int(input("Which level do you want to play? (1- easy, 2- medium, 3- hard) "))
        #calls the game_data function which returns the list of words
        level_list = game_data(levelOfDifficulty)
        print("Here are the words to guess from: ", level_list)
        #getting the random word
        randomWord = random.choice(level_list)

        guess = ''
        turns = 5
        won = False
        #tracks only the right guesses
        hit = ''

        print (name, ", you have 5 turns to guess the word")
        while turns > 0:
            for char in randomWord:
                if char in guess:
                    print(char, end=' ')
                    #Need to record the 'hit' from the guess so the wrong guess will be excluded
                    hit += char
                else:
                    print('_', end=' ')

            #adds letter to the output of the game and if you guessed right then breaks out of loop and prints congrats
            if not won:
                guess = hit 
                print(name, end=', ')
                letter = input("please give me a letter or letters: ")
                guess +=letter
            else:
                print("\nCongratulations! You guessed the word correctly!")
                turns = 0
                break 
            
            #compares the randomWord with the correct guessed values using sets which are 
            if sorted(''.join(set(randomWord))) == sorted(''.join(set(guess))): 
                #if the user guesses the word, we need to set won to true
                won = True
            else: 
                turns -= 1
                print("you have ", str(turns), " turn(s) left")

        game = input(name + " do you want to play again? (yes or no)")

    print(name + ", come back anytime!")
    time.sleep(2)

def main():
    game()

main()