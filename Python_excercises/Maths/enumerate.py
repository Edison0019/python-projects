l = [1,2,3,4,5,6,7,8,9]
def enum(lst):
    c = []
    v = list(enumerate(lst))
    for (i,u) in v:
        c.append(lst[i] ** 2)
    return print(c)

enum(l)