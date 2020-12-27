# Make a program that reads any angle and shows on the screen the value
#  of the sine, cosine, and tangent of that angle.

from math import sin, cos, tan, radians

angle = float(input('Enter the angle you want: '))

print(f'The angle of {angle} has sine of {sin(radians(angle)):.2f}')
print(f'The angle of {angle} has cosine of {cos(radians(angle)):.2f}')
print(f'The angle of {angle} has tangent of {tan(radians(angle)):.2f}')
