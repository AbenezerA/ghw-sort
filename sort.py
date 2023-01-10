sorted = []

def sorter(list):
    list_len = len(list)
    if list_len <= 1:
        return list

    left = sorter(list[:list_len // 2])
    right = sorter(list[list_len // 2:])
    return merger(left, right)

def merger(left, right):
    sorted = []
    len_left = len(left)
    len_right = len(right)

    i = 0; j = 0
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    if i < len_left:
        sorted.extend(left[i:])
    else:
        sorted.extend(right[j:])
    
    return sorted

list = [3, 5, 7, 9, 2, 1, 8, 4]
print(sorter(list)) # Succesfully prints 