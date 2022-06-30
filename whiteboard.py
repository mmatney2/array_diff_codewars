def array_diff(a, b):
    for n in b:
        while n in a:
            a.remove(n)
    return a

print(array_diff([1, 1,2, 2,3], [1, 2]))