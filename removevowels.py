# a function to remove vowels in a string and return the modified string

def mystring(s : str):
    vowels = "AEIOUaeiou"
    result = ""
    
    for char in s :
        if char not in vowels:
            result += char
    return result

print(mystring("Hello"))
print(mystring("Goodbye"))
