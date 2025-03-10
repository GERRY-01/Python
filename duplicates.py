duplicated_list = ["hello", "world","project","duplicate", "world","commit"]

# we want to remove any duplicates in the list

unique_list = []

for word in duplicated_list :
    if word not in unique_list :
        unique_list.append(word)
        
print(f"The list before removing duplicates : {duplicated_list}")
print(f"The list after removing duplicates : {unique_list}")
