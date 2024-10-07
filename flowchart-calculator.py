def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        try:
            choice = int(input("Select operation (1-5): "))
            if choice == 5:
                print("Exiting calculator. Goodbye!")
                break
            
            if choice < 1 or choice > 4:
                print("Invalid input. Please select a number between 1 and 5.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 1:
                result = add(num1, num2)
                operation = "Addition"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = "Multiplication"
            else:
                result = divide(num1, num2)
                operation = "Division"
            
            print(f"{operation} result: {result}")
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        
        restart = input("Do you want to perform another calculation? (yes/no): ").lower()
        if restart != 'yes':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
