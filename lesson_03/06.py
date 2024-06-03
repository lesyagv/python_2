import random

def number_user_game():
    "generate a random number from 1 to 100"
    number = random.randint(1, 100)

    while True:
        user = int(input("Enter a number from 1 to 100: "))
        
        if user == number:
            print("Congratulations!")
            break
        elif user < number:
            print("Your number is too low. Try again.")
        else:
            print("Your number is too high. Try again.")

number_user_game()

