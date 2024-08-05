from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError('Queue is empty')

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError('Queue is empty')

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    # Example of usage

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
