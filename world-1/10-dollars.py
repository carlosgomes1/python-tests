# Make a program that reads how much money the user and owns and shows how many dollars he can have.

money = float(input('Enter how much money you have now: '))

dollars = money * 5.16

print(f'With R${money:.2f} you can have US${dollars:.2f}')
