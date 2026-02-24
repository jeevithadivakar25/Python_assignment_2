#calculating factorial
def factorial(n):
    if n < 0:
        return "Enter number greater than 0!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


#checking Prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#Calculating ffibonacci series
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


#calculating sum of digits
def sum_of_digits(n):
    n = abs(n)   #to handle negative numbers
    total = 0
    
    while n > 0:
        digit = n % 10      #to extract last digit
        total += digit
        n = n // 10         #to remove last digit
    
    return total


#reversing a number
def reverse_number(n):
    
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return reversed_num


#finding Armstrong number
def is_armstrong(n):
    num=n

    # count digits
    count = len(str(n))   # simple way to get number of digits

    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** count
        num //= 10

    return total == n


# GCD
def gcd(a, b):
    pass


# LCM
def lcm(a, b):
    pass


#finding Perfect Number
def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


#main Menu based design
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Prime:", is_prime(n))

        elif choice == "3":
            n = int(input("Enter position: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Armstrong:", is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect Number:", is_perfect_number(n))

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")



math_menu()