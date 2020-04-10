def largest(list):
    x = []
    y = []
    w = None
    for i in list:
        if type(i) == type([]):
            for v in i:
                x.append(v)
            continue
        y.append(i)
    w = x + y
    return max(w)

