# Write a program that reads a value in meters and displays it converted in centimeters and millimeters.

meters = float(input('Enter an value in meters: '))

centimeters = meters * 100
millimeters = meters * 1000

print(f'The value in meters is {meters}')
print(f'The value in centimeters is {centimeters}')
print(f'The value in millimeters is {millimeters}')
