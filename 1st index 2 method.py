def first(a, x, si):
    l = len(a)
    if si == l:
        return -1
    if a[si] == x:
        return si
    small = first(a, x, si + 1)
    return small


a = [1, 2, 3, 45, 4, 7, 5]
print(first(a, 4, 0))
