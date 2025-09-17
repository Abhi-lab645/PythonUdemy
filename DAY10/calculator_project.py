import art

# print(art.logo)

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}





def calculator():

    print(art.logo)

    first_num=float(input("What's the first number?: "))

    should_accumulate=True


    while should_accumulate:

        for operation in operations:
            print(operation)

        operation_symbol=input("Pick an operation: ")

        next_num=float(input("What's the next number?: "))

        answer=operations[operation_symbol](first_num,next_num)

        print(f"{first_num} {operation_symbol} {next_num} = {answer}")

        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice=="y":
            first_num=answer
        else:
            should_accumulate=False
            print("\n" * 20)
            calculator()




calculator()

