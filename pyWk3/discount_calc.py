def calculate_discount(price, discount_percentage):
    if discount_percentage>=20:
        final_price= price*(1-(discount_percentage/100))
        return final_price
    else:
        return price
    
    
def main():
    price=float(input("Enter the item price : "))
    discount_percentage=float(input("Enter the discount percentage : "))
    final_price =calculate_discount(price,discount_percentage)
    print(f"The price is {final_price}")

main()

