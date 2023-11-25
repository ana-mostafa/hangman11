import random

fruit_list = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple']
selected_fruit = random.choice(fruit_list).lower()[0]  # Get the first character of the randomly chosen word

print(selected_fruit)

while True:
    user_guess = input("Please enter a single letter: ")

    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()  # Convert the user's input to lowercase for case-insensitive comparison
        if user_guess == selected_fruit:
            print(f"Good guess! {user_guess} is the first letter of the word.")
            break
        else:
            print(f"Sorry, {user_guess} is not the first letter of the word. Try again.")
    else:
        print("Invalid input. Please enter a single alphabetical character.")
