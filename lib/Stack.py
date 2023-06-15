class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        # else:
        #     raise Exception("Stack is empty")

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        if target not in self.items:
            return -1
        return len(self.items) - self.items.index(target) -1
