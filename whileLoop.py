
x = int(input("enter number x:"))

oddNumber = 0
evenNumber = 0

while x != 0 :
    # print("Im inside while loop")
    if x%2 == 0:
        evenNumber += 1
    else:
        oddNumber += 1

    x = int(input("enter number or 0 to quit while loop:"))
    

print("evenNumber count =",evenNumber)
print("oddNumber count =",oddNumber)