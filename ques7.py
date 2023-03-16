# Write a python script to add a finally block for the above script?
def divide(num1,num2):
    try:
        num3=num1/num2
        
    except ZeroDivisionError:
        print("Can not Divide by Zero")
    finally:
        print(num3)

    #we can not add finally block for the above script because it depend on try block
divide(12,2)
        