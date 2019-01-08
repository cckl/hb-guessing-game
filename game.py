"""A number-guessing game."""
import random
print("Howdy,what's your name?")
print('\n')
name = input('(type in your name) ')
print("{},I'm thinking of a number between 1 and 100.".format(name))
print("Try to guess my number")
secret_number = random.randint(1, 100)

counter = 0
guess = input("Your guess?")

while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high, try again.")
        counter += 1
    elif guess < secret_number:
        print("Your guess is too low, try again.")
        counter += 1
    else:
        print("Well done, {}! You found my number in {} tries!".format(name, counter)

 