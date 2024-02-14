import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1=float(input("enter 1st number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("pick any symbol:")#+
        num2=float(input("enter the next number:"))
        calculator_function=operations_dict[op_symbol]#add
        output=calculator_function(num1,num2)
        print(f"{num1}{op_symbol}{num2}={output}")
        
        should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation or x to exit ").lower()
        if should_continue=="y":
            num1=output
        elif should_continue=="n":
            continue_flag=False
            os.system('cls')
            calculator()
           
        else:
            continue_flag=False
            print("bye")
calculator()
