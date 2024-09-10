def calculate_discount(price, discount_percent):
    def apply_discount(p, d):
        return p - (p * (d / 100))

    if discount_percent >= 20:
        return apply_discount(price, discount_percent)
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying discount
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: ${final_price:.2f}")
