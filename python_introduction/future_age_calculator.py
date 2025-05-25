# Python script that asks the user for their current age and then calculates how old they will be in a specific future year, e.g in 50 years. 
# Using formula: Future Age = Current Age + (Future Year - Current Year)

current_age = int(input("Enter your current age: "))
future_year = 2050  # future year we are calculating for
current_year = 2023
future_age = current_age + (future_year - current_year)
print ( "In", future_year, "you will be", future_age, "years old.")