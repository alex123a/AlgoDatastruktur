A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarysearch(array, start, end, y):
    half = (start + end) // 2
    newArray = []
    if array[half] == y:
        return half
    elif array[half] > y:
        return binarysearch(array, start, half, y)
    elif array[half] < y:
        return binarysearch(array, half, end, y)
    else:
        return -1

print(binarysearch(A, 0, len(A) - 1, 3))

