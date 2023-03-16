a=7
try:
    b=int(input("Enter a number :"))
    c=a/b

except ArithmeticError:
    print("You cannot divide by zero")