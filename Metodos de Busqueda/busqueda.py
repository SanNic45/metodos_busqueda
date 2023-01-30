def linear_search(a, x):
    ix = -1
    for ix, i in enumerate(a):
        if i == x:
            return ix
    return ix

l = [10, 40, 1, 45, 31, 15, 9]
linear_search(l, 40)
