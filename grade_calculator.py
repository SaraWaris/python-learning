marks = float(input("Enter your marks: "))



print("\n------Grade------")
if marks >= 90:
    print("Marks:", marks)
    print("A+")
elif marks >= 80:
    print("Marks:", marks)
    print("A") 
elif marks >= 70:  
    print("Marks:", marks)
    print("B")
elif marks >= 60:
    print("Marks:", marks)
    print("C")
elif marks >= 50:
    print("Marks:", marks)
    print("D")         
else:
    print("Marks", marks)
    print("Grade: Fail")    