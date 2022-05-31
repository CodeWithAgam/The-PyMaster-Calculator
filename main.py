# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from os import system, name
from assets.art import logo


# Functions to carry out the calculations
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def calculator():
    print(logo)

    num1 = float(input("Enter the first number: "))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        
        calculation = operations[operation]
        result = calculation(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start again: ")

        if answer == "y":
            num1 = result

        else:
            should_continue = False
            clear()
            calculator()

calculator()