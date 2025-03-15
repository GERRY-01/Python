# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F

for i in range(6):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    
    print()