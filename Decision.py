name = (input("Enter your name: "))
subject1 = int(input("Enter mark of S1: "))
subject2 = int(input("Enter mark of S2: "))
subject3 = int(input("Enter mark of S3: "))
subject4 = int(input("Enter mark of S4: "))
subject5 = int(input("Enter mark of S5: "))
total = subject1+subject2+subject3+subject4+subject5
average = (total/5)
attendance = int(input("Enter your Attendance: "))
income = int(input("Enter annual income: "))

print("____STUDENT DETAIL----")
print("Name:", name)
print("Total:",total,"/500")
print("Average:", average)

if average > 85 :
       print("Grade A")
    
elif average > 75:
       print("Grade B")
       
elif average > 65 :
       print("Grade C")
      
elif average > 55:
       print("Grade D")
       
elif average > 40:
       print("Grade E")
       
else:
       print("Grade F")

if attendance > 75 and income < 200000:
       print("Elegible for Scholarship")
else:
       print("Not elegible for Scholarship")
