#Ask user how many times they want to roll the dice

import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    #num_of_rolls = int(input("How many times would you like to roll the dice?: ")) (trying to do optional enhancement #1)
    if choice == "y":
        roll_1 = random.randrange(1,7)
        roll_2 = random.randrange(1,7)
        rolls = (roll_1, roll_2)
        print(rolls)

    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")




