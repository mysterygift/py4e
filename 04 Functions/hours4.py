print("Welcome to the Paycheck Calculatron 9001.\n")
def computepay(hours, rate) :
    try:
        try:
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
            print("Your pay this week is",pay)
        except:
            print("I don't like letters :( Numbers only please!")
            quit()
    except:
        print("I don't like letters :( Numbers only please!")
        quit()
    return pay

print (computepay(300, 40))