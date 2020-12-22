# Make a program that reads the height and width of a wall,
# calculates its area and the amount of paint needed to paint it,
# knowing that each liter of paint paints 2m²

width = float(input('Enter the width of the wall: '))
height = float(input('Enter the height of the wall: '))

area = width * height
paint = area / 2

print(f'The area of this wall is {area:.2f}m²')
print(f'You are going to need {paint:.2f} liters of paint')
