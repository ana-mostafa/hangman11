import random

def validate_input(guess):
    if isinstance(guess, str) and len(guess) == 1 and guess.isalpha():
        print('Good guess!')
    else:
        print('Oops! That is not a valid input')

fruit_list = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple']
selected_fruit = random.choice(fruit_list)

print(selected_fruit)

user_guess = input("Please enter a single letter: ")
validate_input(user_guess)
