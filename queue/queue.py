"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from collections import deque

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = deque([])
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)
        return value

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.popleft()


my_queue = Queue() 

print(my_queue.enqueue('first'))

print(len(my_queue))
print(my_queue.enqueue('second'))
print(len(my_queue))
print(my_queue.enqueue('third'))
print(len(my_queue))
print(my_queue.dequeue())
print(len(my_queue))
print(my_queue.dequeue())
print(len(my_queue))
print(my_queue.dequeue())
print(len(my_queue))
print(my_queue.dequeue())
print(len(my_queue))
print(len(my_queue))
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

