# myList = [1,5,8,200,4,"test"]
# print(myList[3])

# myList[4] = 900
# print(myList)

# myList[0] = myList[2]
# print("new myList :",myList)

# print("lenght of myList:", len(myList))

# myStr = "abcdef"
# print("lenght of myStr:", len(myStr))
# print("myStr[3]:", myStr[3])

# print("slice myStr [1:] -->", myStr[:-1])


myList = []

for i in range(5):
    myList.append(i)

print("myList append:", myList)


myList1 = []

for i in range(5):
    myList1.insert(i,i+5)

print("myList1 insert:", myList1)