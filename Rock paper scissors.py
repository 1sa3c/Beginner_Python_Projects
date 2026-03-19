import random

emojis = {"r" : "🪨", "p" : "📃", "s" : "✂️"}
computer_submit = random.choice(("r", "p", "s"))

while True:
    submission = input("Rock, paper, or scissors? (r/p/s): ").lower()
    while submission not in ("r", "p", "s"):
        print("Invalid choice!")
        submission = input("Rock, paper, or scissors? (r/p/s): ").lower()
    else:
        print(f"You selected: {emojis[submission]} | The computer selected: {emojis[computer_submit]}")
    if submission == computer_submit:
        print("Draw!")
    elif (
        (submission == "r" and computer_submit == "s") or
        (submission == "s" and computer_submit == "p") or
        (submission == "p" and computer_submit == "r")):
        print("User wins!")
    else:
        print("Computer wins!")
    replay = input("Do you want to play again? (y/n): ").lower()
    while True:
        if replay == "n":
            print("Game over.")
            break
        elif replay == "y":
            break
        else:
            print("Invalid syntax, please respond with either 'y' or 'n'")
            replay = input("Do you want to play again? (y/n): ").lower()
    if replay == "n":
        break

#Hold on, I'm just testing to see if this does anything on GitHub. Doing it again real quick.