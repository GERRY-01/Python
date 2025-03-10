my_string = input("Enter any string: ")

count = 0
vowels = "aeiouAEIOU"

for char in my_string :
    if char in vowels :
        count += 1
print(f"There are {count} vowels in {my_string}")
        
        