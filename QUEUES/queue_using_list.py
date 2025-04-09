class Queue:
    def __init__(self, value):
        self.queue = [value]
        self.length = 1
    
    def print_queue(self):
        for i in self.queue:
            print(i)
    
    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1
    
    def dequeue(self):
        value = self.queue[0]
        self.queue.pop(0)
        self.length -= 1
        return value

queue = Queue(4)
queue.print_queue()

print("**************************")
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.print_queue()

print("**************************")
value = queue.dequeue()
print("value dequeued:", value)
value = queue.dequeue()
print("value dequeued:", value)
value = queue.dequeue()
print("value dequeued:", value)
value = queue.dequeue()
print("value dequeued:", value)
queue.print_queue()