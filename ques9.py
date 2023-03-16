def Raise_Error():
    x = input("Enter a number : ")

    if not x.isdigit():
        raise ValueError("Invalid input: Enter a Positive integer")

    print("You entered :", x)

Raise_Error()