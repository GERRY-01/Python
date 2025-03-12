def reverse(sent:str):
    reversed_sent = ""
    
    for char in sent:
        reversed_sent = char + reversed_sent
    return reversed_sent

print(reverse("you are a bad boy"))