# create a list of words, we are going to pick one random word, we ask the useer to guess that word
#input, random, time to delay
import random
import time
#import os

# ask user for information
name = input("What is your name? ")
print(name, ", Welcome to our game!")

# create a list of words 
# pick a random word
# get the user to guess the word with different levels of difficulty
#wordList = ['python', 'java', 'php', 'ram', 'computer', 'keyboard']
game = input("Do you want to play? ")

dict = {}
easy_list = []

#print("=====>"+os.getcwd())
#file1 = open('/Users/kayleechien/OneDrive - Greenhill School/DataScience/RandomFile.txt',"r")
file1 = open("RandomFile.txt","r")
line1 = file1.readline()
print(line1)
#line2 = file1.readlines()
#print(line2)

while game == 'yes':
    levelOfDifficulty = input("Which level do you want to play? (easy, medium, hard) ")       
    #splitting the file into keys and values
    for i in line1:
        (key,val) = i.split()
        dict[a] = val
    print(dict)
    

    #getting the values of the dictionary aka the words into its own list
    word_list = list(dict.values())
    print(word_list)

    if levelOfDifficulty == "easy" or levelOfDifficulty == "Easy":
        for i in range(key.count('easy')):
            #get list of all of the words correlated with easy
            easy_list.append(word_list[i]) 
        print(easy_list)
        word = random.choice(easy_list)
    #word = random.choice(wordList)
        guess = ' '
        turns = 5
        print ("you have 5 turns to guess the word")
        while turns > 0:
            for char in word:
                if char in guess:
                    print(char, end= '')
                else:
                    print('_', end = ' ')
            print()
            letter = input("please give me a letter: ")
            guess += letter
            turns -= 1
        game = input("Do you want to play again? ")
print(name, ", Come back anytime!")
time.sleep(5)






