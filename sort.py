import merge

# Recursive method to keep splitting list into halves
def sorter(list):
    list_len = len(list)
    if list_len <= 1:
        return list

    left = sorter(list[:list_len // 2])
    right = sorter(list[list_len // 2:])
    return merge.merger(left, right)

# Test case
list = [3, 5, 7, 9, 2, 1, 8, 4]
print(sorter(list))
