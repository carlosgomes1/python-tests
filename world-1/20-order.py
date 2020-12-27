# The same teacher of challenge 019 wants to draw the order of presentation of students'
#  papers. Make a program that reads the names of the four students and shows the order drawn.

from random import shuffle

student1 = input('First student: ')
student2 = input('Second student: ')
student3 = input('Third student: ')
student4 = input('Fourth student: ')

studentList = [student1, student2, student3, student4]

shuffle(studentList)

print(f'The order of presentation will be: \n{studentList}')
