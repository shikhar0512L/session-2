name = str(input("Enter you name: "))
age = int(input("Enter your age: "))
gpa  = float(input("Enter your GPA: "))

age_to_float = float(age)
gpa_to_int = int(gpa)
print(age_to_float,gpa_to_int)

new_age = age>20
new_age_bool = bool(new_age)
print(new_age_bool)
