
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else: 
        return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("\n=== CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting Calculator...")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = modulus(a, b)
            elif choice == "6":
                result = power(a, b)

            print("Result:", result)

        else:
            print("Invalid choice! Please select 1-7.")


if __name__ =="__main__":
    calculator()