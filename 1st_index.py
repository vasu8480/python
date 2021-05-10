def first(a,n):
    l=len(a)
    if l==0:
        return -1
    if a[0]==n:
        return 0
    small=a[1:]
    smallout=first(small,n)
    if smallout ==-1:
        return -1
    else:
        return smallout+1
a=[1,2,3,45,4,7,5]
print(first(a,4))