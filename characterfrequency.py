#  a program to count the frequency of each character in a string using a dictionary.

my_string = input("Enter your string: ")

char_count = {}

for char in my_string :
    if char in char_count :
        char_count[char] += 1
    else :
        char_count[char] = 1

# print character frequencies

for char, count in char_count.items():
    print(f"{char} : {count}")