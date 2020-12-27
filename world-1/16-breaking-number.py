# Create a program that reads any Real number by keyboard and shows your entire part on the screen.

from math import trunc

number = float(input('Enter a float number: '))

print(
    f'The value entered was {number} and its entire share is {trunc(number)}')
