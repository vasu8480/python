def replace(s, a, b):
    if len(s) == 0:
        return s
    small = replace(s[1:], a, b)
    if s[0] == a:
        return b + small
    else:
        return s[0] + small


print(replace("vasuvasu", 'v', 'p'))
