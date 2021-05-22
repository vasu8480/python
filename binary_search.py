def binary(a, x, si, ei):
    if si > ei:
        return -1
    mid = (ei + si) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary(a, x, si, mid - 1)
    else:
        return binary(a, x, mid + 1, ei)


print(binary([1, 2, 3, 4, 5, 6, 7], 3, 3, 6))
