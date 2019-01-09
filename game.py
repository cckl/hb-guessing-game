"""A number-guessing game."""
import random
print("Howdy, what's your name?")
print('\n')
name = input('(type in your name) ')
print("{},I'm thinking of a number between 1 and 100.".format(name))
print("Try to guess my number")
secret_number = random.randint(1, 100)

counter = 0
while True:
    try:
        guess = int(input("Your guess? "))
        break
    except ValueError:
        print("Please enter a valid integer!")
       


while True:
    if int(guess) > 100 or int(guess) < 1:
        print ('Sorry, please enter a number between 1 and 100!')
        guess = int(input("Your guess? "))

    elif guess > secret_number:
        print("Your guess is too high, try again.")
        counter += 1
        guess = int(input("Your guess? "))
    elif guess < secret_number:
        print("Your guess is too low, try again.")
        counter += 1
        guess = int(input("Your guess? "))
    else:
        print("Well done {}! You found # in {} tries!".format(name, counter))
        break


