# A funcion accepting 2 lists and returning their common elements

def lists(list1, list2):
    for item in list1 :
        for values in list2:
            if item == values :
                return item
                
print(lists(["Hello", "world"], ["Doctor", "world"]))