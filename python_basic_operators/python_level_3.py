# Q18. Salary Calculator
# Take an employee's basic salary as input.
# Calculate:
# HRA = 20% of basic salary
# DA = 10% of basic salary
# Bonus = 5% of basic salary
# Gross salary = Basic salary + HRA + DA + Bonus
# Display all components and the final gross salary.
sal = input("Enter your basic salary : ")
sal = int(sal)
print("Your salary is : " + str(sal))
print("Your HRA is : " + str(0.2 * sal))
print("Your DA is : " + str(0.1 * sal))
print("Your bonus is : " + str(0.05 * sal))
print("Your Gross salary is : " + str(sal + 0.35 * sal))

# Q19. Shopping Discount Calculator
# Take the following inputs:
# Original price
# Quantity purchased
# Discount percentage
# Calculate:
# Total price before discount.
# Discount amount.
# Final amount payable.
org_price = int(input("Enter the original price : "))
qty = int(input("Enter the qty : "))
dsc = float(input("Enter the discount(in %) : "))
print("The Total price before discount is : " + str(org_price * qty))
print("The Total discount is : " + str(((org_price * qty) * (dsc/100))))
print("The Total price after discount is : " + str((org_price * qty) - ((org_price * qty) * (dsc/100))))

# Q20. Operator Precedence Challenge
# Without executing the code first, predict the output of each expression. Then verify your answers in Python.
# a = 10 + 5 * 2b = (10 + 5) * 2c = 20 / 5 + 3d = 20 // 6 + 2 ** 3e = 10 % 3 * 2
# Print the values of a, b, c, d, and e.
a = 10 + 5 * 2 #20
print(a)
b = (10 + 5) * 2 #30
print(b)
c = 10 + 5 * 2 ** 2 #30
print(c)
d = 20 // 6 + 2 ** 3 #11
print(d)
e = 10 % 3 * 2 #2
print(e)

# Q21. Age Calculator
# Ask the user to enter their birth year and the current year.
# Calculate their approximate age by subtracting the birth year from the current year.
# Display the result in a sentence.
yob = int(input("Enter year of birth : "))
curr = int(input("Enter current year : "))
print("Age is : " + str(curr - yob))

# Q22. Water Bill Calculator
# Take the number of units of water consumed as input.
# Calculate the bill using the following rates:
# First 100 units: ₹2 per unit
# Next 100 units: ₹3 per unit
# Above 200 units: ₹5 per unit
# Assume a progressive billing system: each rate applies only to the units within its respective range.
# Display the total bill.
# Hint: This question can initially be solved using arithmetic operators and variables. For the complete solution, conditional statements will also be required.
units = int(input("Enter the units consumed : "))
bill_100 = 0
bill_200 = 0
bill_final = 0
if units <= 100:
  bill_100 = units * 2
elif units >=100 and units <= 200:
  bill_200 = 200 + ((units - 100) * 3)
else:
  bill_final = 500 + ((units - 200) * 5)
print("the final bill : " + str(bill_100 + bill_200 + bill_final))



# Q23. Boolean and Comparison Challenge
# Predict the output of the following code:
# a = 10b = 20c = 15print(a < b)print(b > c)print(a == c)print(a < b and b > c)print(a > b or c > a)print(not(a == b))
# Explain why each expression returns True or False.
a = 10
b = 20
c = 15
print(a < b) #TRUE
print(b > c) #TRUE
print(a == c) #FALSE
print(a < b and b > c) #TRUE
print(a > b or c > a) #TRUE
print(not(a == b)) #TRUE

# Q24. Final Challenge: Restaurant Bill Splitter
# Write a Python program that accepts:
# Food bill amount
# GST percentage
# Tip percentage
# Number of people splitting the bill
# Calculate:
# GST amount.
# Tip amount, calculated on the original food bill.
# Total bill including GST and tip.
# Amount each person must pay.
# Ensure that the number of people is greater than zero.
#24
food_bill = float(input("Enter the food bill : "))
gst = float(input("Enter the GST percentage : "))
tip = float(input("Enter the tip percentage : "))
ppl = float(input("Enter the number of people : "))
gst_amt = (food_bill * gst) / 100
tip_amt = (food_bill * tip) / 100
total_bill = gst_amt + tip_amt + food_bill
amt_per_head = total_bill / ppl
print("The GST amount is : " + str(gst_amt))
print("The tip amount is : " + str(tip_amt))
print("The total bill is : " + str(total_bill))
print("The amount per head : " + str(amt_per_head))
