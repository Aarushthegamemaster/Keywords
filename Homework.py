due_amount = int(input("Please enter the amount of money you owe:"))
money_paid = int(input("Please enter the amound of money you paid:"))

if due_amount > money_paid:
    money_owed = due_amount - money_paid
    print("The amount of money you owe is", money_owed)
    pass
else:
    print("You are debt free!")