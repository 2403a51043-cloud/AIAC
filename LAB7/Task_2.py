
# The current code will raise a TypeError because you can't compare int and str in Python 3.
# To correct it, we can sort by converting all items to strings, or provide a key function.
def sort_list(data):
    return sorted(data, key=str)

items = [3, 'apple', 1, "banana", 2]
print(sort_list(items))
