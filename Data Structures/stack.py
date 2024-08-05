class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    # Example of usage
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    print(s.pop())
    print(s.pop())
