print("Welcome to the Paycheck Calculatron 9000.\n")
hours = input("Please enter the number of hours worked this week: ")
rate = input("What is the rate of pay per hour?: ")
pay = float(hours) * float(rate)
round(pay,2)
print("Calculating...\n")
print("Your pay this week is ",pay)