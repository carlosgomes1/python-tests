# Write a program that asks how many miles a rental car has traveled and
#  the amount of days it has been rented. Calculate the price to pay, knowing
#  that the car costs R $ 60 per day and R $ 0.15 per km wheeled.

days = int(input('How many rented days? '))
km = float(input('How many kms run? '))

pay = (days * 60) + (km * 0.15)

print(f'The total to be paid is R${pay:.2f}')
