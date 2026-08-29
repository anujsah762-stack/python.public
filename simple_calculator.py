def calculator():
    """Simple calculator that performs basic arithmetic operations"""
    print("=" * 40)
    print("         SIMPLE CALCULATOR")
    print("=" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (**)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ('1', '2', '3', '4', '5'):
            print("Invalid choice! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
