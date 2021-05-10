n = int(input())


def print_qto_n(n):
    if n == 0:
        return
    print_qto_n(n-1)
    print(n)
    return
print(print_qto_n(n))

def print_nto_1(n):
    if n == 0:
        return
    print(n)
    print_nto_1(n - 1)

    return
print(print_nto_1(n))
