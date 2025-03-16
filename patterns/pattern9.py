# 1
# 2 6 
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

n = 5
for i in range(1,n+1):
    num = i
    for j in range(i):
        print(num,end=" ")
        num += n-j-1
        
    print()