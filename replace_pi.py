def pi(s):
    if len(s) == 0 or len(s) == 1 or len(s) == 2:
        return s
    if s[0] == 'p' and s[1] == 'i' and s[2] == 'i':
        small = pi(s[3:])
        return '3.14' + small
    else:
        small = pi(s[1:])
        return s[0] + small


print(pi("piippii"))

