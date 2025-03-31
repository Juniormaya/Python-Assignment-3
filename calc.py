def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    :param price: The original price of the item.
    :param discount_percent: The discount percentage to be applied.
    :return: The final price after applying the discount.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    # Return the original price if discount is less than 20%
    return price

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the results
if final_price != price:
    print(f"The final price after applying a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied, the final price is the same as the original price.")