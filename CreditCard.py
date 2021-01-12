"""
This program prompts the user for a credit card number
Then shows whether it is valid for American Express, MasterCard, Visa, or Discover card
"""

def creditCard():
    credit_card_number = input("What is your credit card number? ")

    #retrieving the first digit or zeroth index of the credit card number
    first_digit_card = credit_card_number[0]

    #The user's input is considered a string, so comparison needs to be with a string/char not int
    #The first digit of mastercards is 2 or 5
    #The first digit of american express cards is 3 
    #The first digit of visas is 4
    #The first digit of discover cards is 6
    if first_digit_card == '2' or first_digit_card == '5':
        print("Your credit card is a valid MasterCard!")
    elif first_digit_card == '3':
        print("Your credit card is a valid American Express Card!")
    elif first_digit_card == '4':
        print("Your credit card is a valid Visa Card!")
    elif first_digit_card == '6': 
        print("Your credit card is a valid Discover Card!")
    else:
        print("This is not a valid credit card number.")

creditCard()