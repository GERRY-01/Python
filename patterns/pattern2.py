""" this pattern 
     A 
    A B 
   A B C 
  A B C D 
 A B C D E 
A B C D E F 

"""
n = int(input("How many rows of alphabets do you want to be printed: "))

for i in range(n):
    for k in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(chr(65+j), end=" ")
        
        
    print()
        
