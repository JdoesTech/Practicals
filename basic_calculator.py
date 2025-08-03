def switch_option(a,b):
    option = int(input("Select your operation"))
    match option:
        case 1:
            return (a+b)
        case 2:
            return (a-b)
        case 1:
            return (a*b)
        case 1:
            return (a/b)
        
def operation():
    a = int(input("Add first number"))
    b = int(input("Add second number"))
    switch_option(a,b)

def main():
    operation()
        