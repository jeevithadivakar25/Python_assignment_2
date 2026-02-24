#taking user inputs
day = input("Enter day of week: ").strip().lower()
num_tickets = int(input("Enter number of tickets: "))

total_base = 0

for i in range(1, num_tickets + 1):
    age = int(input(f"Enter age for person {i}: "))

    #Calculating age-based Pricing
    if age < 3:
        price = 0
        category = "Free"
    elif age <= 12:
        price = 150
        category = "Child"
    elif age <= 59:
        price = 300
        category = "Adult"
    else:
        price = 200
        category = "Senior"

    print(f"Person {i}: {category} - ₹{price}")
    total_base += price

#/calculating day-based Discount
if day in ["friday", "saturday", "sunday"]:
    discount_percent = 20
else:
    discount_percent = 0

discount_amount = total_base * discount_percent / 100
final_amount = total_base - discount_amount

#final Output
print("\n=== TICKET BILL ===")
print("Total base price: ₹", total_base)
print("Discount:", discount_percent, "%")
print("Discount amount: ₹", round(discount_amount, 2))
print("Final amount to pay: ₹", round(final_amount, 2))