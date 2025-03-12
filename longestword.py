def longestword(sent: str) :
    word = ""
    longest = 0
    
    for char in sent:
        if char != " ":
            word += char
        else:
            if len(word) > longest :
                longest = len(word)
            word = ""
    if len(word) > longest :
        longest = len(word)
 
    return longest

print(longestword("john the baptist"))