def duplicate(s : str):
    result = ""
    for char in s:
        if char not in result:
            result +=char
    return result
    
print(duplicate("yooooh"))