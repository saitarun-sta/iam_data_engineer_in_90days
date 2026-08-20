x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
operation = input("Enter operation e.g., (+ , - , / , *) : ")

match operation:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "/":
        if y != 0:
            print(x / y)
        else:
            print("Cannot divide by zero.")
    case "*":
        print(x * y)
    case _:
        print("Invalid Opeartion")