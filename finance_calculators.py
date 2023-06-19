import math

# Title of program
print("\nFinancial Calculator\n")

# print out the 'financial calculator menu' for the user to choose from
# Found in stack overflow - as well as .upper .lower can use .casefold (removes all case sensitivity in strings).
print("1. Investment - to calculate the amount of interest you'll earn on your investment")
print ("2. Bond - to calculate the amount you'll have to pay on a home loan")

# Created a variable 'finance_option' to hold user selection
finance_option = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").casefold()

# Based on the 'user choice', applied if/elif statements to perform calculations
if  finance_option == "investment": 
    deposit = float(input("\nYou have selected investment.\nHow much money do you want to deposit: £"))
    interest_rate = float(input("Enter the percentage interest rate: "))
    years = float(input("Enter the number of years you are investing for: ")) 
    interest = input("Do you want 'simple' or 'compound' interest?: ").casefold()

    if interest == "simple":
        # Calculate the total amount with simple interest
        total_amount_s = deposit * (1 + (interest_rate / 100) * years)
        print(f"\nThe total amount you will get back from your investment incl. interest is £{total_amount_s: }")
      
    elif interest == "compound":
        # Calculate the total amount with compound interest
        total_amount_c = deposit * math.pow(1 + (interest_rate / 100), years)
        print(f"\nThe total amount you will get back from your investment incl. interest is {total_amount_c: }")

elif finance_option == "bond":
    value = float(input("\nYou have selected bond.\nWhat is the current value of your house: £ "))
    interest_rate = float(input("Enter the percentage interest rate: "))
    months = float(input("Enter number of months needed to repay bond: "))
    
    monthly_interest = (interest_rate / 100) / 12
    repayment = (monthly_interest * value) / (1 - (1 + monthly_interest) ** (-months))
    print(f"\nTherefore, You will need to pay back £{repayment: } per month")

else:
    # If user enters something other than "investment" or "bond"
    print("You have not entered investment or bond.")




