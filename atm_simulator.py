# Initial account condition
balance = 10000   
MIN_BALANCE = 500

#Menu based design
while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        
        #deposit logic
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("New balance: ₹", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        
        #withdrawal logic
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
        elif balance - amount < MIN_BALANCE:
            print("Withdrawal denied! Minimum balance of ₹500 must be maintained.")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("New balance: ₹", balance)

    #exiting program logic
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")