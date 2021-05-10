a= [1,2,3,5,4]
def  sorted(a):
    l =len(a)
    if l==0 or l==1:
        return True
    if a[0] >a[1]:
        return False
    smalllist =a[1:]
    smallsorted=sorted(smalllist)
    if smallsorted:
        return True
    else :
        return False
print(sorted(a))