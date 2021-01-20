#question 1
def list_sum():
    myList = [1, 50, 300, 43, 26]
    #using built-in sum function finds the sum of the items in the list
    print(sum(myList))

#question 2
def count_elements():
    countString = "lkseropewdssafsdfafkpwe"
    #create empty strings for initialization for the most common chars and the one that deletes the repeats
    commonList = []
    realList= []
    #going through each character in the string to see which is most common
    total_occur = 0
    character = countString[0]

    #getting the most commonly occured characters and how often the occur
    for i in countString:
        current_occur = countString.count(i)
        #example shows the characters that have at least 3 occurances
        if current_occur > 2:
            total_occur = current_occur
            character = i 
            #adding a tuple into the list
            commonList.append((i, total_occur))

    #deleting the duplicate instances
    for i in commonList:
        if i not in realList:
            realList.append(i)
    print(realList)

#question 3
def concat_dict():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}
    dic4 = {}
    #adding each dictionary to the empty dictionary
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
    print(dic4)

#question 4
def count_strings():
    stringDup = ['abc', 'xyz', 'aba', '1221']
    count = 0
    #restricions are if the string is longer than two characters and the first and last characters are the same
    #count those strings
    for i in stringDup:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    print(count)

#question 5
def distinct_words():
    numWords = input("Input number of words: ")
    theWords =[]

    #getting the inputed words into one list to find the distinct words
    for i in range(int(numWords)):
        words = input("Enter word: ")
        theWords.append(words)    

    distinctList = []
    count = 0
    occurance = 0

    #finding the number of distinct words by comparing them in the theWords list and count
    for i in theWords:
        if i not in distinctList:
            distinctList.append(i)
            count += 1
    print(count, end = ' ')

    #getting the occurances for each word by counting each instance of the word in theWords list
    for word in distinctList:
        occurance = theWords.count(word)
        print(occurance, end = ' ')

#question 6
def remove_duplicates():
    duplicateList = [1, 2, 5, 5, 6, 2, 2, 4, 10, 11]
    noDuplicates = []
    #remove duplicates by adding elements from duplicateList to noDuplicates
    #then comparing if an element is already there then don't add
    for i in duplicateList:
        if i not in noDuplicates:
            noDuplicates.append(i)
    print(" ")
    print(noDuplicates)


list_sum()
count_elements()
concat_dict()
count_strings()
distinct_words()
remove_duplicates()
