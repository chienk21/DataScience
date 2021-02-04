import json
import random
 
#gets the words from the dictionary in the file and randomizes the words
#the length of the word is less than the set length and the word is greater than 2
#returns the word that is randomized
def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word

#shuffles the word and then compares the shuffled word to the actual word
def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        #shuffle the list of the letters in the word
        random.shuffle(array)
        #then joins so that it will be in the form of the word with no spaces
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled

#getting json file
if __name__ == "__main__":
    filename = 'Anagrams/dictionary_data.json'
    file = open(filename)
    #json.load takes a file object and returns the json object
    data = json.load(file)
    
    #plays the game
    print("Welcome to the Anagram Game!")
    while(True):
        word = word_prompt(data, 5)
        question = shuffle_word(word)

        #this gets the values of the dictionary in the file
        meaning = data[word]
        
        question = question.lower()
        word = word.lower()
        
        print("\nSolve:", question)
        print("Hint:", meaning)

        #first two numbers are the parameters and the third number is 
        #what increment it's moving down at
        for i in range(5, 0, -1):
            print("\nAttempts Left:", i)
            guess = input('Make a guess: ').lower()
            if guess == word:
                print("Correct!")
                break
            if i == 1:
                print("\nCorrect Answer:", word)
        
        choice = input("\nContinue? [y/n]: ")
        #line separater
        print('-'*50)

        if choice == 'n':
            print("\nThank you for playing!")
            break