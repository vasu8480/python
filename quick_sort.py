def part(a, si, ei):
    pivot = a[si]
    c = 0
    for i in range(si, ei + 1):
        if a[i] < pivot:
            c = c + 1
    a[si + c], a[si] = a[si], a[si + c]
    pi_ind = si + c
    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i = i + 1
        if a[j] >= pivot:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    return pi_ind


def quick(a, si, ei):
    if si >= ei:
        return
    pi_ind = part(a, si, ei)
    quick(a, si, pi_ind - 1)
    quick(a, pi_ind + 1, ei)


a = [6, 4, 5, 8, 11, 54, 25, 64]
print(a)
print(part(a, 0, len(a) - 1))
print(a)
print(quick(a, 0, len(a) - 1))
print(a)


