# Write a python script to implement try except and else block for division?
def Divide():
    try:
        num1=int(input("Enter first number :"))
        num2=int(input("Enter second number :"))
        
        num3=num1/num2
    except ValueError:
        print("Please enter a int type Number")
    except ZeroDivisionError:
        print("You can not divide by Zero!")
    else:
        print(num3)

Divide()