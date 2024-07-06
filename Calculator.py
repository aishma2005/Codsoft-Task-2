# Function to add two numbers
def addition(x, y):
    return x + y

# Function to subtract two numbers
def subtraction(x, y):
    return x - y

# Function to multiply two numbers
def multiplication(x, y):
    return x * y

# Function to divide two numbers
def division(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

# Function to display the menu of operations
def menu():
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

# Main function to run the calculator
while True:
    menu()
    choice = input("Enter your choice from 1-5: ")

    if choice in ['1', '2', '3', '4']:
            # Get user input for two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
                
            if choice == '1':
                result = addition(num1, num2)
                print(f"Result: {result}")
            elif choice == '2':
                result = subtraction(num1, num2)
                print(f"Result: {result}")
            elif choice == '3':
                result = multiplication(num1, num2)
                print(f"Result: {result}")
            elif choice == '4':
                result = division(num1, num2)
                print(f"Result: {result}")
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        
    elif choice == '5':
        print("Exiting Application...")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")