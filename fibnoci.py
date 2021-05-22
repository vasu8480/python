def fib(n):
    if n==1 or n==2 :
        return 1
    fib1=fib(n-1)
    fib2=fib(n-2)
    out = fib1+fib2

    return out
n=int(input())
print(fib(n))