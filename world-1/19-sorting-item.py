#  A teacher wants to draw one of his four students to erase the board.
# Make a program that helps him by reading the students' names and writing on the screen
# the name of the chosen one.

from random import choice

student1 = input('First student: ')
student2 = input('Second student: ')
student3 = input('Third student: ')
student4 = input('Fourth student: ')

studentList = [student1, student2, student3, student4]

chosen = choice(studentList)

print(f'The student chosen was {chosen}')
