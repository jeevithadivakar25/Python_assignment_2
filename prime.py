#function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#Part 1 solution

#taking single input
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a PRIME number")
else:
    print(f"{num} is NOT a prime number")


#Part2 aolution

#taking a range input
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:")

#using for loop to find the prime numbers
for number in range(start, end + 1):
    if is_prime(number):
        print(number)
