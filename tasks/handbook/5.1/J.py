class Stack:

    lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def is_empty(self):
        if not self.lst:
            return True

