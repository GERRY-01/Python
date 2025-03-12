n = int(input("Enter the number of terms: "))

def fibonacci(nterms):
    a,b = 0,1
    fibonacci_seq = []
    for _ in range(nterms):
        fibonacci_seq.append(a)
        a, b = b, a+b
    return fibonacci_seq
            
if n <= 0 :
    print("Enter only positive numbers")
else:
    print(fibonacci(n))