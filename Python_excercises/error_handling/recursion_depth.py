def recursion_depth(number):
    print('recursion depth number',number)
    try:
        recursion_depth(number + 1)
    except:
        print('it is not possible to execute above the number')