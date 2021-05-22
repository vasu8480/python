a=[1,2,3,4,6,5,7]
def sorted(a,si):
    l = len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    small=sorted(a,si+1)
    return small
print(sorted(a,5))
