year = int(input("Enter the year:"))



print("\n-----Leap Year-----")
if year % 400 == 0:
    print(" Leap Year")
elif year % 100 == 0:
    print("Not a Leap Yera")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a leap year")        