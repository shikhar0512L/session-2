# a=True
# b="3"
# c='Hello'

# d=float(b)
# e=str(b)
# f=bool(b) # TODO: False -> identify
# print(d,e,f)

# ? Create a Python program that asks the user for their personal information and performs some basic calculations.
name = str(input("Enter you name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

age_in_months = 12*age
height_in_cm = 100*height

print("Your name is: ",name)
print("Your age in months is: ",age_in_months)
print("Your height in cm is: ",height_in_cm)
