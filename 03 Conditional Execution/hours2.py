print("Welcome to the Paycheck Calculatron 9001.\n")
hours = input("Please enter the number of hours worked this week: ")
rate = input("What is the rate of pay per hour?: ")
frate = float(rate)
fhours = float(hours)
if (fhours > 40):
    print("Overtime :(")
    overtime = fhours - 40
    fovertime_rate = float(rate) * 1.5
    pay = (40 * frate) + (overtime * fovertime_rate)
else:
    print("Boring normal pay lol")
    pay = fhours * frate
round(pay,2)
print("Calculating...\n")
print("Your pay this week is ",pay)