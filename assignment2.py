list_words = []
with open('romeo.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word not in list_words:
                list_words.append(word)
list_words.sort()
for word in list_words:
    print(word)
