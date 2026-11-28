total = 0
above = 0
for i in range(1,8):
    expense = int(input(f"Enter the expense of day {i}: "))
    total = total + expense
    if expense > 200:
       above += 1
average_expense = total/7

print("----Weekly expense----")
print("Total expense:$",total)
print("average      :",average_expense)
print("Above 200    :", above)
