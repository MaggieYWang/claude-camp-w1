#This is a Tip Calculator - Input the meal amount and tip percentage, then output the total amount

#Enter the meal amount
meal_amount = float(input("How much did you pay? $"))
print(f"You paid ${meal_amount:,.2f}")

#Enter tip percentage
tip_percentage = float(input("Enter tip percentage: %"))

#Calculate total amount
total = meal_amount * (1 + tip_percentage/100)
print(f"The total amount is ${total:,.2f}")
