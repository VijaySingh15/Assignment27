class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    try:
        def __sub__(self):
            self.c=self.a-self.b
            return self.c
        def __add__(self):
            self.c=self.a+self.b
            return self.c
        def __mul__(self):
            self.c=self.a*self.b
            return self.c
        def __div__(self):
            self.c=self.a/self.b
            return self.c
    except ZeroDivisionError:
        print("Not divide by zero")
    except ValueError:
        print("do not enter a invalid value")
    except ArithmeticError:
        print("overflow or another problem")
    except Exception:
        print("another type error")

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
c1=Calculator(num1,num2)
print(c1.__add__())
print(c1.__sub__())
print(c1.__div__())
print(c1.__mul__())