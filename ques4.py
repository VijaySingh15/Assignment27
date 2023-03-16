a=7
try:
    b=int(input("Enter number :"))
    c=a/b
except ValueError:
    print("Enter number not string")