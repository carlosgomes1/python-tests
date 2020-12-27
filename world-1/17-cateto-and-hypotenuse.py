# Make a program that reads the length of the opposite cateto and the adjacent catheter of a
# right triangle. Calculate and show the length of the hypotenuse.

from math import hypot

opposite = float(input('Length of opposite cateto: '))
adjacent = float(input('Length of adjacent cateto: '))

hypotenuse = hypot(opposite, adjacent)

print(f'The hypotenuse will measure {hypotenuse:.2f}')
