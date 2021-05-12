def last(a, x):
    l = len(a)
    if l == 0:
        return -1
    small = a[1:]
    smallout = last(small, x)
    if smallout != -1:
        return smallout + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1


a = [1, 2, 3, 45, 4, 7,3]
x = 3
print(last(a, x))
