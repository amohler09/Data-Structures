"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
# not needed with array? --> self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        return self.storage.tail.value

    def pop(self):
        if self.storage.tail != None:
            self.size -= 1
            return self.storage.remove_tail()
       
            

my_stack = Stack() 
print(my_stack.push('first'))
print(len(my_stack))
print(my_stack.push('second'))
print(len(my_stack))
print(my_stack.push('third'))
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(len(my_stack))
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())



