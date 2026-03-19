import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess any number between 1 and 100: "))
    except (ValueError, TypeError, NameError):
        print("Please enter a valid number")
    if number_to_guess < guess:
        print("Too high")
    elif number_to_guess > guess:
        print("Too low")
    else:
        print("Well done!")
        break


print("Didn't really have time today")
print("Same as yesterday :(((((")
#same as the past 2 days unfortunately.