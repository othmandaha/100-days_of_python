"""A calculator program"""
from Ascii_calculator import calc
from os import system

def add(a, b):
    """Returns the addition of a and b."""
    return a + b

def multiply(a, b):
    """Returns the multiplication of and b."""
    return a * b

def subtract(a, b):
    """Returns the subtraction b from."""
    return a - b

def divide(a, b):
    """Retruns the division of a with b."""
    return a / b

operations = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divide
}

def calculator():
    """A function that does simple calculations."""
    answer = "c"
    i = 0
    while answer == "c":
        i += 1
        print(calc)
        if i == 1:
            num1 = float(input("Type the first number: "))
        else:
            num1 = result
            print("The first number is {}".format(num1))
        num2 = float(input("Type the second number: "))

        for symbol in operations:
            print("{}".format(symbol))

        symbol = input("Chose you operation from the above operations: ")

        function = operations[symbol]
        result = function(num1, num2)

        print("The result of the operation: {} {} {} = {}\n".format(num1, symbol, num2, result))

        answer = input("Type 'c' to continue calculating with the result: {}\n"
                        "Type 'n' to start a new  calculation\n"
                        "Type 'e' to exit the program\n".format(result))
        system("cls")
        if answer == "n":
            calculator()


if __name__ == "__main__":
    calculator()
