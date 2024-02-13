class Queue:

    lst = []

    def push(self, item):
        self.lst.append(item)
        return self.lst

    @classmethod
    def pop(cls):
        return cls.lst.pop(0)

    @classmethod
    def is_empty(cls):
        if not cls.lst:
            return True


queue = Queue()
print(queue.push(5))
print(queue.push(9))
queue1 = Queue()
print(queue1.push("fgggd"))
