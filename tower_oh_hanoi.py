def tower(n, a, b, c):
    if n == 1:
        print("move 1st from", a, "to", c)
        return
    tower(n - 1, a, c, b)
    print("move", n, "the disk from", a, "to", c)
    tower(n - 1, b, a, c)
print(tower(4, "s", "a", "d"))
