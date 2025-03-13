# Printing the most frequent element in a list

cities = ["Nairobi","Cape Town","Harare","Nairobi","Rabat"]

city_count = {}

for item in cities:
    if item not in city_count:
        city_count[item] = 1
    else:
        city_count[item] += 1

largest_count = 0
most_frequent_element = ""

for key,value in city_count.items():
    if value > largest_count :
        largest_count = value
        most_frequent_element = key
        
print(most_frequent_element)