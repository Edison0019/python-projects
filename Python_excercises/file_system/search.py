def search(xs,comp):
    for (i,v) in enumerate(xs):
        if v == comp:
            return i
    return -1

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

print(search(friends,'Joe'))