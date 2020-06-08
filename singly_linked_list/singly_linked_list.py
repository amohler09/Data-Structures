# In a linked list, each space in memory can be looked at as taking up a value plus the next node (pointer)
# What do we need to be able to access with our Node class though?
# In our Node class, we can now get the value of our node, get the next value, and set the next value
class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


# In the linked list, we need to define our head and tail
# What behavior should our list be able to do?
    # Add to the tail and remove the head
class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    # We need to be able to add to the tail
    def add_to_tail(self, value):
        # The value that gets passed in needs to be a node
        # (wrap the input value in a node)
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head
        # If the list is initially empty, set both head and tail to the new node
        # Linked lists with ONE item would have the same head and tail
          self.head = new_node
           self.tail = new_node
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # Is there is a head?
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # Check if there is a next value
        # If head has no next, there is only a single element in the linked list
        # So we can just return the head & set the head and tail to None
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head
​
        while current.get_next() is not self.tail:
       current = current.get_next()
​
        value = self.tail.get_value()
        self.tail = current
            return value

    def contains(self, value):
    if not self.head:
        return False
​
  # Recursive solution
  # def search(node):
  #   if node.get_value() == value:
  #     return True
  #   if not node.get_next():
  #     return False
  #   return search(node.get_next())
  # return search(self.head)

  # get a reference to the node we're currently at; update this as we traverse the list
  current = self.head
   # check to see if we're at a valid node
   while current:
        # return True if the current value we're looking at matches our target value
        if current.get_value() == value:
            return True
        # update our current node to the current node's next node
        current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False
​
  def get_max(self):
       if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value
