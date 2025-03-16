# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

for i in range(5):
    num = i+1
    for j in range(5-i):
        print(num, end=" ")
        num +=1
    print()