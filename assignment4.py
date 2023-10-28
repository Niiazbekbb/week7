numbers = [] 
count = 0  
total = 0  
while True:
    user_input = input("Please enter an integer: ")
    if user_input == 'done':
        break
    try:
        num = int(user_input)
        total += num
        count += 1
        numbers = numbers + [num]  
        average = total / count
        print(f"{numbers} , average = {average:.2f}")
    except ValueError:
        print("Please enter an integer!")
print("Bye-bye !!!")
