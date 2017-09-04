#first object in is first object out
#First in, first out
# add object to end, remove from front
# Queues in real life: Notification services
#Interface: provides simple way to input/output (ie keyboard to computer)
#Methods:
# enqueue (append node to end of list)
# dequeue --return first node

class Node:
    def __init__(self, value, below=None):
        self.value = value
        self.previous = below
    

class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def peek(self):
        # Return the next node
        return self.first
    
    def dequeue(self):
        #remove the first element and return it 
        node_to_return = self.first

        if node_to_return == self.last:
            self.last = None
            self.first = None
        else:
            self.first = self.first.previous

        return node_to_return
    
    def enqueue(self, value):
        #Add new node to the end of the queue
        new_node = Node(value)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.previous = new_node
            self.last = new_node

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(5)
print(queue.dequeue().value)
print(queue.dequeue().value)