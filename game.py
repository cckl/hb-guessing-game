"""A number-guessing game."""
import random
print("Howdy,what's your name?")
print('\n')
name = input('(type in your name) ')
print("{},I'm thinking of a number between 1 and 100.".format(name))
print("Try to guess my number")
secret_number = random.randint(1, 100)


