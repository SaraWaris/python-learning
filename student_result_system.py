name = (input("Enter Student name: "))
total_marks = float(input("Enter total marks:"))
obtained_marks = float(input("Enter obtained marks: "))
percentage = (obtained_marks/total_marks)*100

print("\n-----Student Result-----")
print("Name:", name)
print("Percentage:", percentage)

if percentage >= 90:
    print("A+,Excellent")
elif percentage >= 80:
    print("A,very Good") 
elif percentage >= 70:  
    print("B, Good")
elif percentage >= 60:
    print("C, Need Improvement")
elif percentage>= 50:
    print("D, Do More Effort")     

print("Percentage:", percentage)    
if percentage >=40:
   print("pass")
else:
    print("fail")