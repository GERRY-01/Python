word  = input("Enter any word: ")

empty_dict = {}

for char in word:
    if char not in empty_dict:
        empty_dict[char] = 1
    else:
        empty_dict[char] += 1
    
for key,value in empty_dict.items():
    print(f"{key} : {value}")