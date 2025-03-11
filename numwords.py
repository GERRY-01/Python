# we use strip to ignore any spaces before and after the sentence
sentence = input("Enter a sentence: ").strip()

count = 1

if len(sentence) == 0 :
    count = 0
else :
    for i in range(len(sentence)-1) :
        if sentence[i] == " " and sentence[i+1] != " ":
            count += 1
                
print(count)