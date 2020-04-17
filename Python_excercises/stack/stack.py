class stack:
    def __init__(self):
        self.items = []
    def push(self,el):
        self.items.append(el)
    def pop(self):
        self.items.pop()
    def is_empty(self):
        return self.items == []