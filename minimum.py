# given a list of numbers, find the maximum and minimum values

mylist = [48, 63, 12, 77, 92, -4, 108]

maximum = mylist[0]
minimum = mylist[1]

for num in mylist :
    if num > maximum :
        maximum = num
    if num < minimum :
        minimum = num
        
print(f"maximum number is {maximum}")
print(f"minimum number is {minimum}")