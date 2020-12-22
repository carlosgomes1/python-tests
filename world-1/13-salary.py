# Make an algorithm that reads an employee's salary
# and shows on the screen your new salary with a 15% increase.

salary = float(input('Enter the old salary: '))

newSalary = salary * 1.15

print(f'Old salary: R${salary:.2f}')
print(f'New salary: R${newSalary:.2f}')
