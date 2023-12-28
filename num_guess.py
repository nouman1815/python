print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')
import random
the_correct_guess= random.randint(1,100)
print(the_correct_guess)
def hard():
    chances = 5


    while chances!=0:

        print(f"you have {chances} attempts to guess the number \n")
        guess = int(input("make a guess\n"))
        chances -= 1
        # if chances>=1:
        #     print("guess again")

        def correct():

            print(f"you have guessed the right number {guess}")

        #
        if guess == the_correct_guess:
            correct()
            chances = 0
        #
        def too_high():

            print("too high")

        #
        if guess >the_correct_guess:
            too_high()

        #
        #
        def too_low():

            print("too low")

        #
        if guess < the_correct_guess:
            too_low()

        if chances>=1:
            print("guess again")
    print("you have ran out of guesses YOU LOOSE")


def easy():
    chances = 10

    while chances != 0:

        print(f"you have {chances} attempts to guess the number \n")
        guess = int(input("make a guess\n"))
        chances -= 1

        # if chances>=1:
        #     print("guess again")

        def correct():

            print(f"you have guessed the right number {guess}")

        #
        if guess == the_correct_guess:
            correct()
            chances = 0

        #
        def too_high():

            print("too high")

        #
        if guess > the_correct_guess:
            too_high()

        #
        #
        def too_low():

            print("too low")

        #
        if guess < the_correct_guess:
            too_low()

        if chances >= 1:
            print("guess again")
    print("you have ran out of guesses YOU LOOSE")

level=input("Choose a difficulty. Type 'easy' or 'hard':\n")
if level=='hard':
    hard()
elif level=='easy':
    easy()