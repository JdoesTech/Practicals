operands_list = ["+","-","*","/"]

def operate():
    a= int(input("Enter first value : "))
    b= int(input("Enter second value : "))
    while True:
        operand= input("Select operand")
        if operand in operands_list:
            match operand:
                case "+":
                    result=a+b
                case "-":
                    result=a-b
                case "*":
                    result=a*b
                case "/":
                    if b ==0:
                        print("Invalid calculation: divisor cannot be zero")
                        return None
                    result=a/b
            print(f"{a}{operand}{b} = {result}")
            return result
            break
        else:
            print("Input a valid operand")

def main():
    operate()

main()