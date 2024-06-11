# i = 6

# for i in range (5):
#     print(i)

# print("outside for loop. ", i)

# for i in range (2,5):   #(start,end)
#     print(i)

# print("outside for loop. ", i)

# for i in range (2,10,2):   #(start,end,incrementVal)
#     if i == 6:
#         break
#     print("inside for loop. ", i)

# print("outside for loop. ", i)

for i in range (20):   #(start,end,incrementVal)
    if i == 6 or i%2 > 0:
        continue
    print("inside for loop. ", i)

print("outside for loop. ", i)



