balance = 10000
withdrawal = int(input("Enter the amount: "))
Remaining_balance = balance - withdrawal
Withdrawal_percentage = (withdrawal/balance)*100
Equal_share = Remaining_balance/2
Total_balance = balance/2

print("-----ATM TRANSACTION----")
print("Inital Balance: ", balance)
print("Withdrawal: ", withdrawal)
print("Balance: ", Remaining_balance)
print("Withdrawal Percentage: ", Withdrawal_percentage)
print("Equal share: ", Equal_share)
print("Total Balance: ", Total_balance)