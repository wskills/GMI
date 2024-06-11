
# myVar = 20
# my_var = "50"
# myFloat = 20.3

# print("enter any value and press enter:")
# myInput = input("enter any value and press enter:")

# print(myVar,my_var,myFloat, sep = "--")

# print(myVar*5,my_var*3,sep="--")

# print("myInput-->", myInput)

print("This is a BMI calculator.")
height = float(input("Enter your height in meter:"))
weight = float(input("Enter your weight in kg:"))

bmi = weight/height**2
underweight = 18.4
normal = 24.9
overweight = 39.9

print("Your BMI:", bmi)

if bmi <= underweight:
    print("Underweight")

elif bmi <= normal:
    print("normal")

elif bmi <= overweight:
    print("overweight")

else:
    print("obese")
