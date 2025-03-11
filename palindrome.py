# a python function to check if a given string is palindrome

def palindrome(s : str) :
    s = s.lower()
    length  = len(s)
    
    for i in range(length // 2) :
        if s[i] != s[length - i - 1] :
            return False
        else:
            return True
        
print(palindrome("Level"))        
print(palindrome("Hello"))