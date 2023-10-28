count = 0
with open('mbox.txt', 'r') as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if len(words) > 1:
                sender = words[1]
                print(sender)
                count += 1
print(f'Total lines printed: {count} ')
