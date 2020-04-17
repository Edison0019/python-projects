#the koch problem shows how to organize a line based on the order of the problem 1,2,3 and so on.
#this problem along with the turtle module shows how to draw a line based on the different orders

def koch(t,size, order):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60,-120,60,0]:
            koch(t,size / 3,order - 1)
            t.left(angle)
