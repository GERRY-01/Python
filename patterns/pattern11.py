# 7 6 5 4 3 2 1 
# 7 6 5 4 3 2 
# 7 6 5 4 3 
# 7 6 5 4 
# 7 6 5 
# 7 6 
# 7 

row = int(input("Enter the number of rows to be printed: "))

for i in range(row):
    num = row
    for j in range(row-i):
        print(num, end=" ")
        num -=1
    print()