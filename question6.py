expenses = [250, 1200, 450, 800, 150, 2000, 350]
count=0
Total=sum(expenses)
print("Total Expense:",Total)
average=Total /len(expenses)
print("Average Expense:",average)
print("Highest Expense:",max(expenses))
print("Lowest Expenses:",min(expenses))
for i in expenses:
    if i>500:
        count+=1
        print("No of Expenses Greatern than 500",count)
    if i>average:
        print("Expenses Above Average:",i)
