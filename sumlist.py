# sum of all positive numbers in a list

list1 = [14, 24, -6, 29, -5, -7, 17]

count = 0

for num in list1 :
    if num > 0:
        count += num
print(count)