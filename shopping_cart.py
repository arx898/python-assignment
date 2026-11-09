# Problem 2: Simple Shopping Cart

customer = input("Enter customer name: ")

product1 = input("Enter name of product 1: ")
price1 = float(input(f"Enter price of {product1}: "))

product2 = input("Enter name of product 2: ")
price2 = float(input(f"Enter price of {product2}: "))

product3 = input("Enter name of product 3: ")
price3 = float(input(f"Enter price of {product3}: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    rate = 0.20
elif subtotal >= 3000:
    rate = 0.10
elif subtotal >= 1000:
    rate = 0.05
else:
    rate = 0.0

discount = subtotal * rate
final_total = subtotal - discount


def fmt(value):
    """Show whole numbers without decimals, otherwise 2 decimal places."""
    return f"{value:.0f}" if value == int(value) else f"{value:.2f}"


print()
print(f"Customer Name: {customer}")
print(f"Product 1: {product1}")
print(f"Price: {fmt(price1)}")
print(f"Product 2: {product2}")
print(f"Price: {fmt(price2)}")
print(f"Product 3: {product3}")
print(f"Price: {fmt(price3)}")
print(f"Subtotal: {fmt(subtotal)}")
print(f"Discount: {fmt(discount)}")
print(f"Final Total: {fmt(final_total)}")
