sorted = []

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