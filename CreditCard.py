"""
This program prompts the user for a credit card number
Then shows whether it is valid for American Express, MasterCard, Visa, or Discover card
"""

def creditCard():
    credit_card_number = input("What is your credit card number? ")
    first_digit_card = credit_card_number[0]
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