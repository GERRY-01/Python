# A program to find the sum of digits in a number

num = int(input("Enter a number: "))

sum = 0
while num > 0 :
    last_digit = num % 10
    sum += last_digit
    num = num // 10

print(sum)