mylist = [4,7,2,9,1,12,6]

# Assume the largest number is at index 0
largest = mylist[0]

for num in mylist :
    if num > largest :
        largest = num
        
print(largest)
    