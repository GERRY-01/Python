num = int(input("Enter your number: "))

if num < 2 :
    print("Not a prime number")

else : 
    for i in range(2,num) :
        if num % i == 0 :
            print("Not a prime number")
            break
            
    else: 
        print("a prime number")