list_words = []
with open('romeo.txt', 'r') as file:
    for line in file:
        list_words.extend(line.split())
list_words = sorted(set(list_words))
for word in list_words:
    print(word)

