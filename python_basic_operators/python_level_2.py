# Swap Two Variables
# Take two numbers as input and swap their values using a third variable. Print the values before and after swapping.
x,y = 10,20
p,q = y,x
print("Before Swapping the values were : " + str(x) + "and" + str(y))
print("After Swapping the values were : " + str(p) + "and" + str(q))

# Q11. Student Marks Calculator
# Accept marks for five subjects from the user.
# Calculate and display:
# Total marks
# Average marks
# Percentage, assuming each subject is out of 100
English = int(input("Enter your marks for English :"))
Math = int(input("Enter your marks for Math :"))
Science = int(input("Enter your marks for Science :"))
Social_Studies = int(input("Enter your marks for Social Studies :"))
Hindi = int(input("Enter your marks for Hindi :"))
Total = English + Math + Science + Social_Studies + Hindi
print("Total marks : " + str(Total))
print("Avg is : " + str(Total/5))
print("Your percentage is : " + str((Total/500)*100) + "%")

# Q12. Comparison Operators
# Take two numbers as input and check whether:
# The first number is greater than the second.
# The first number is smaller than the second.
# Both numbers are equal.
# The numbers are not equal.
# The first number is greater than or equal to the second.
# Display the results as Boolean values.
x = input("Enter first number : ")
y = input("Enter second number : ")
print("The first number is greater than the second:" + str(x>y))
print("The first number is smaller than the second:" + str(x<y))
print("Both numbers are equal:" + str(x==y))
print("The numbers are not equal:" + str(x!=y))
print("The first number is greater than or equal to the second:" + str(x>=y))

# Q13. Even or Odd Using Modulus
# Take an integer as input and use the modulus operator to determine whether it is even or odd.
x = int(input("Enter your first integer: "))
if x%2 == 0:
  print("Even")
else:
  print("Odd")
# Q14. Assignment Operators
# Create a variable x = 20. Perform the following operations one after another:
# Add 5 using an assignment operator.
# Subtract 3 using an assignment operator.
# Multiply by 2 using an assignment operator.
# Divide by 4 using an assignment operator.
# Print the value of x after every operation.
x=20
print(x)
x+=5
print(x)
x-=3
print(x)
x*=2
print(x)
x/=2
print(x)
# Q15. Logical Operators
# Take a person's age and ask whether they have a driving licence (True or False).
# Check whether the person:
# Is at least 18 years old.
# Has a driving licence.
# Meets both conditions.
Age = int(input("Enter Age : "))
Licence = input("Do you have DL (True/False): ")
Licence = Licence == "True"
print("is at least 18 years old : " , Age >= 18)
print("Has driving license : ",Licence )
print("Meets both Conditions : ",Age >=18 and Licence )

# Q16. Shopping Bill Calculator
# Take the price and quantity of three products as input.
# Calculate:
# Total cost of each product.
# Total bill.
# Average cost per product unit, assuming the total quantity is greater than zero.
pen_price = int(input("Enter Price of pen :"))
book_price = int(input("Enter Price of book :"))
cup_price =  int(input("Enter Price of cup :"))
pen_qty = int(input("Enter Qty of pen :"))
book_qty = int(input("Enter Qty of book :"))
cup_qty =  int(input("Enter Qty of cup :"))
pen_cost = pen_price * pen_qty
book_cost = book_price * book_qty
cup_cost = cup_price * cup_qty
total_bill = pen_cost + book_cost + cup_cost
avg_cost = round(total_bill / (pen_qty + book_qty + cup_qty) ,2)
print("total pen cost : " + str(pen_cost))
print("total book cost : " + str(book_cost))
print("total cup cost : " + str(cup_cost))
print("total bill : " + str(total_bill))
print("Avg Cost per unit : " + str(avg_cost))


# Q17. Data Type Conversion
# Create the following variables:
# a = "25"b = "10.5"c = 5d = 2.5
# Perform these tasks:
# Convert a into an integer.
# Convert b into a float.
# Convert c into a string.
# Convert d into an integer.
# Print all converted values and their data types.
# Explain why converting "10.5" directly into an integer causes an error.
a = "25"
b = "10.5"
c = 5
d = 2.5
p = int(a)
q = float(b)
r = str(c)
s = int(d)
print(p)
print(type(p))
print(q)
print(type(q))
print(r)
print(type(r))
print(s)
print(type(s))
print(int(float("10.5")))
