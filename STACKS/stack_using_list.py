class Stack:
    def __init__(self, value):
        self.stack = [value]
        self.height = 1
    
    def print_stack(self):
        for i in self.stack:
            print(i)
    
    def push(self, value):
        self.stack.append(value)
        self.height += 1

    def pop(self):
        value = self.stack[-1]
        self.stack.pop()
        self.height -= 1
        return value
    


stack = Stack(4)

stack.print_stack()
print("***************************")
stack.push(5)
stack.push(7)
stack.push(8)
stack.push(9)
stack.print_stack()
print("***************************")
value = stack.pop()
print("value popped:", value)
value = stack.pop()
print("value popped:", value)
value = stack.pop()
print("value popped:", value)
value = stack.pop()
print("value popped:", value)
stack.print_stack()