expenses = []
num_expenses = int(input("Enter # of expenses"))
total = 0

for i in range(num_expenses):
    expenses.append(float(input("Please enter an amount: ")))

total = sum(expenses)
#for x in expenses:
#    sum = sum + x

print("You spent $", total, sep = '')