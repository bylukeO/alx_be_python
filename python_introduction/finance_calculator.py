# python script to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.
# Using formula: Monthly Savings = Monthly income - Monthly expenses
# Future Savings = Monthly Savings * Number of months

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are:", monthly_savings)

# Projected annual savings based on monthly savings assuming a simple annual rate of 5%
print("Your projected annual savings is:", monthly_savings * 12)

# Future savings based on a 5% annual interest rate over 1 year using the formula (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
future_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is", future_savings)