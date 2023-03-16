def nested():
    try:
        num1=int(input("Enter first number :"))
        num2=int(input("Enter second number :"))
        
        try:
            division=num1/num2
            print("Division is :",division)

        except ZeroDivisionError:
            print("You cant not divide by Zero")

    except ValueError:
        print("Please Enter a Integer type value")
nested()