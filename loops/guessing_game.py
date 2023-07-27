import random

play_again = "y"

while play_again == "y":
    random_number = random.randint(1, 10)
    user_num = int(input("Pick a number from 1 and 10 "))

    while user_num != random_number:
        if user_num < 1 or user_num > 10:
            user_num = int(input("Your guess is out of range, pick a number from 1 and 10 "))
        elif user_num < random_number:
            user_num = int(input("Too low, guess again "))
        else:
            user_num = int(input("Too high, guess again "))

    print(f"{user_num} is the correct guess!")
    play_again = input("Would you like to play again? y/n ")
    