from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def push(self, item):
        self.queue1.put(item)
    
    def pop(self):
        if self.queue1.qsize() == 0:
            return None
        
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        popped_item = self.queue1.get()
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_item

stack = StackUsingQueue()
stack.push(1)
stack.push(2)
print(stack.pop())  
print(stack.pop())  
stack.push(3)
print(stack.pop())  
