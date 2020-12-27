# Write a program that converts a temperature by typing to degrees Celsius
#  and convert to Degrees Fahrenheit.

celsius = float(input('Enter a temperature in Cº: '))
fahrenheit = (celsius * (9 / 5)) + 32

print(f'{celsius}ºC equals {fahrenheit}ºF')
