class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop() if len(self.items) > 0 else None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        pass

    def search(self, target):
        pass
