#taking user inputs
number = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)

#final multiplication logic
for i in range(1, end + 1):
    print(f"{number} x {i} = {number * i}")