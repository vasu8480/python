n = int(input())

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
def sum(n):
    if n==0:
        return 0
    small = sum(n-1)
    out=small+n
    return out
print(fact(n))
print(sum(n))