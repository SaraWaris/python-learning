pin = input("Enter the pin:")

if pin == "1234":
    amount = float(input("Enter amount:"))
    if amount <= 5000:
        print("Transaction Successful!")

    else: 
            print("Insufficient balance!")
else:
    print("Invalid PIN!")            

