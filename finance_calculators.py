import math

# program that allows the user to access two different financial calculators: an investment calculator and a home loan (bond) repayment calculator

print ("\n")
print ('Financial Calculator \n')


# 1.    Calculation: Investment
#           options: simple and compound

while True:
    calculation = input("investment  - to calculate the amount of interest you'll earn on your investment \n"
                        "bond        - to calculate the amount you'll have to pay on a home loan \n"
                        "\n"
                        "Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if calculation == "investment":
        print("\n")
        P = int(input ("Enter the amount of money to deposit: "))
        r = int(input ("Enter the interest rate: ")) / 100    
        t = int(input ("Enter the number of years you plan on investing: "))

# Simple:   interest is continually calculated on the initial amount invested and is only calculated once per year.
# Compound: interest is calculated on the current total known as the accumulated amount.

        while True:
            print("\n")
            interest = input("Enter one of the interest options: 'simple' or 'compound': ").lower()
            print("\n")
            if interest == str("simple"):
                A = P*(1 + r*t)
                print ("The total amount when simple interest is applied: " + str(A))
                break
            elif interest == str("compound"):   
                A = P * math.pow((1 + r), t)
                print ("The total amount when compound interest is applied: " + str(A))
                break
            else:
                print ("Please, enter one of the interest options: 'simple' or 'compound': \n")

# 2.    Calculation: Bond (Home Loan)

    elif calculation == "bond":
        print("\n")
        P = int(input("Enter the actual value of the house: "))
        i = int(input("Enter the interest rate: ")) / 100 / 12
        n = int(input("Enter the number of months planned to repay the bond: "))
        repayment = (i * P)/(1 - (1 + i)**(- n))
        print("\n")
        print ("Your monthly payment will be :" + str(repayment))
        break
    else: 
        print("Sorry, something went wrong!")
    print("\n")