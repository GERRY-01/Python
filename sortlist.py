list = [18,12,29,7,63,21,44,32]

#result = []
for i in range(len(list)-1):
    if list[i] > list[i+1] and i+1 < len(list):
        list[i],list[i+1] = list[i+1], list[i]
print(list)
