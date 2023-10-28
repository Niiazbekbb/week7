def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
    else:
        lst.clear()
def middle(lst):
    if len(lst) >= 3:
        return lst[1:-1]
    else:
        return []
my_list = [10, 20, 30, 40]
print("my list before calling chop function =>", my_list)
chop(my_list)
print("my list after calling chop function =>", my_list)
my_list = [10, 20, 30, 40]
print("\nmy list before calling middle function =>", my_list)
result = middle(my_list)
print("my list after calling middle function =>", my_list)
print("new list after calling middle function =>", result)
