import math

def add():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(x + y)

def subtract():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(x - y)

def multiply():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(x * y)

def divide():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(x / y)

def square():
    x = float(input("Enter a number: "))
    print(x ** 2)

def cube():
    x = float(input("Enter a number: "))
    print(x ** 3)

def square_root():
    x = float(input("Enter a number: "))
    print(math.sqrt(x))

def factorial():
    x = float(input("Enter a number: "))
    print(math.factorial(int(x)))

def cm():
    x = float(input("Enter a number: "))
    print(x * 2.54)

def inches():
    x = float(input("Enter a number: "))
    print(x / 2.54)

def sine():
    x=float(input("Enter angle: "))
    print(math.sin(x))

def cosine():
    x=float(input("Enter angle: "))
    print(math.cos(x))

def tengant():
    x=float(input("Enter angle: "))
    print(math.tan(x))

def cosec():
    x=float(input("Enter angle: "))
    print(1/math.sin(x))

def sec():
    x=float(input("Enter angle: "))
    print(1/math.cos(x))

def cot():
    x=float(input("Enter angle: "))
    print(1/math.tan(x))

def log():
    x = float(input("Enter a number: "))
    print(math.log())

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square") 
print("6. Cube") 
print("7. Square Root")
print("8. Factorial")
print("9. Centimeters to Inches")
print("10. Inches to Centimeters")
print("11. Sine")
print("12. Cosine")
print("13. Tangent")
print("11. Cosec")
print("12. Sec")
print("13. Cot")
print("14. Log")
choice = int(input("Enter your choice: "))

if choice == 1:
    add()   

elif choice == 2:
    subtract()

elif choice == 3:
    multiply()

elif choice == 4:
    divide()

elif choice == 5:
    square()

elif choice == 6:
    cube()

elif choice == 7:
    square_root()

elif choice == 8:
    factorial() 

elif choice == 9:
    cm()    

elif choice == 10:
    inches()

elif choice == 11:
    sine() 

elif choice == 12:
    cosine()    

elif choice == 13:
    tengant()

elif choice == 11:
    cosec() 

elif choice == 12:
    sec()    

elif choice == 13:
    cot()

elif choice == 14:
    log()

else :
    print("Try again")