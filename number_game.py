import random

def game():
    # Generate a random number between 1 - 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # Get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isnt a number!".format(guess))
        else:
            # Compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        print("You didnt get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again?: Y/n\t")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye")

game()
