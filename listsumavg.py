#taking user inputs
count = int(input("How many numbers? "))

numbers = []

#taking list inputs
for i in range(1, count + 1):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

# Calculation part
total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

#final outputs
print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)