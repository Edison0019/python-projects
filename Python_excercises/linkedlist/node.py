class node:
    def __init__(self,cargo=None,next=None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        return str(self.cargo)

#this prints the elements of the list of nodes backward
"""def print_bk(list):
    if list is None: return
    head = list
    tail = list.next
    print_bk(tail)
    print(head,end=' ')"""