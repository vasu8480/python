def last(a,x,si):
    l=len(a)
    if si==l:
        return -1
    smallout=last(a,x,si+1)
    if smallout !=-1:
        return smallout
    else:
        if a[si]==x:
            return si
        else:
            return -1
a = [1, 2, 3, 45, 4, 7,3]
x = 3
print(last(a, x,1))