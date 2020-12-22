# Make an algorithm that reads the price of a product and shows its new price with 5% discount.

price = float(input('Enter the price of the product: '))

print(
    f'The product that cost R${price:.2f}, with 5% discount, now costs {(price * 0.95):.2f}')
