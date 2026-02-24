def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not possible for negative numbers.")
else:
    result = factorial(num)
    print(f"{num}! = {result}")