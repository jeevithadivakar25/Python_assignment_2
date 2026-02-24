

# Inputs from the user
total_bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

#calculation part
subtotal = total_bill
tax_amount = subtotal * tax_percent / 100
after_tax = subtotal + tax_amount
tip_amount = after_tax * tip_percent / 100
total_amount = after_tax + tip_amount
per_person = total_amount / people

#final output
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal:    ₹{subtotal}")
print(f"Tax ({tax_percent}%):   ₹{tax_amount}")
print(f"After tax:   ₹{after_tax}")
print(f"Tip ({tip_percent}%):   ₹{tip_amount}")
print(f"Total:       ₹{total_amount}")
print(f"Per person:  ₹{per_person}")