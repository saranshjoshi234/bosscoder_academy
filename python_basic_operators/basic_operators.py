# Create two variables, a = 25 and b = 10. Perform and print:
# Addition
# Subtraction
# Multiplication
# Division
# Floor division
# Modulus
# Exponentiation

a = 25
b = 10
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a|b)
print(a**b)


# Calculate Rectangle Area
# Take the length and breadth of a rectangle as input. 
# Calculate and display its area and perimeter.

Length = input("Enter the length(in cm) : ")
Breadth = input("Enter the breadth(in cm) : ")
Area = int(Length) * int(Breadth)
Perimeter = 2 * (int(Length) + int(Breadth))
print("the area is : " + str(Area) + "cm2")
print("the perimeter is :" + str(Perimeter) + "cm")


# Take the temperature in Celsius as input and convert it into Fahrenheit.


Temp = input("Enter temp in celcius : ")
print("The temperature is : " + str(round((int(Temp) * (9/5) + 32),2)) + " Fahrenheit")


# Take principal, rate, and time as input. Calculate the simple interest.

P = int(input("Enter your principal value: "))
R = float(input("Enter ROI: "))
T = int(input("How many years of interest: "))
print("The SI will be : " + str((P * R * T)/100) )