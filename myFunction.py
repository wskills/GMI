# def message(number=100):
#     print("message from function with parameter",number)

# message(50)
# message(60)
# message(70)
# message()

# def bmi(weight,height):
#     bmiVal = weight/height**2
#     print("Your bmi is", round(bmiVal,2))

# bmi(60,1.65) #positional parameter

# bmi(height=1.7, weight=65) #keyword argument passing


def bmi(weight,height):
    bmiVal = weight/height**2
    return bmiVal

valFun = bmi(70,1.6)

valFun += 2

print(valFun)
