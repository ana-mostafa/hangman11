#task1
while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

#task2
import random

fruit_list = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple']
selected_fruit = random.choice(fruit_list).lower()  # Convert the word to lowercase for case-insensitive comparison

print(selected_fruit)

while True:
    user_guess = input("Please enter a single letter: ")

    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()  
        if user_guess in selected_fruit:
            print(f"Good guess! '{user_guess}' is in the word.")
            break
        else:
            print(f"Sorry, '{user_guess}' is not in the word. Try again.")
    else:
        print("Invalid input. Please enter a single alphabetical character.")

#task3
import random

def check_guess(guess):
    selected_fruit = random.choice(fruit_list).lower()  
    guess = guess.lower()
    
    if guess in selected_fruit:
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        user_guess = input("Please enter a single letter: ")

        if len(user_guess) == 1 and user_guess.isalpha():
            if check_guess(user_guess):
                break
        else:
            print("Invalid input. Please enter a single alphabetical character.")

# Get the list of words
fruit_list = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple']

ask_for_input()

