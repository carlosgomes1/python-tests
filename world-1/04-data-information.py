# Make a program that receives something and informs as much information as possible.

answer = input('Enter something: ')

print(f'The primitive type of this value is {type(answer)}')
print('Is there only spaces? {}'.format(answer.isspace()))
print('Is a number? {}'.format(answer.isnumeric()))
print('Is it alphabetical? {}'.format(answer.isalpha()))
print('Is it alphanumerical? {}'.format(answer.isalnum()))
print('Is upper? {}'.format(answer.isupper()))
print('Is lower? {}'.format(answer.islower()))
print('Is it capitalized? {}'.format(answer.istitle()))
