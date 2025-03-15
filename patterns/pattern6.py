#             1
#           1 2
#         1 2 3
#       1 2 3 4
#     1 2 3 4 5
#   1 2 3 4 5 6
# 1 2 3 4 5 6 7

for i in range(7):
    for j in range(7-i-1):
        print(" ",end="")
        
    for j in range(i+1):
        print(1+j,end="")
        
    print()