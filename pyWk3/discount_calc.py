def calculate_discount(price, discount_percentage):
    if discount_percentage>=20:
        final_price= price*(1-(discount_percentage/100))
        return final_price
    else:
        return price
        
    
def main():
    try:
        price = float(input("Enter the item price: "))
        discount_percentage = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount.")
        exit()
        
    try:
        if price <0 or discount_percentage <0:
            raise ValueError("Entered values must be non-negative.")
        if discount_percentage >100:
            raise ValueError("Discount percentage cannot exceed 100.")
    except ValueError as ve:
        print(ve)
        exit()
    
        
    final_price =calculate_discount(price,discount_percentage)
    if final_price<price:
        print(f"The price after discount is {final_price}")
    else: 
        print(f"No discount was applied. The price is {final_price:.2f}")
    

main()

