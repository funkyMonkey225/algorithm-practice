class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class myLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #adds new value to end of list
    def append(self, value):
        new_node = Node(value)
        #if head and tail are none, assign head and tail to new value
            #if false: assign new node to current tail's next property, reassign current tail to new node
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, value):
        #Find value, 
        # if value exists, assign previous node's next value to next next node
        #else, return
        current = self.head
        while current != None and current.next.value != value:
           current = current.next
        if current.next == None:
            return
        
        node_needed = current.next
        current.next = node_needed.next
        node_needed.next = None

        if node_needed == self.tail:
            self.tail = current

    
    def output(self):
        output = []
        current = self.head
        while current != None:
            print(current.value)
            output.append(current.value)

            current = current.next
        return output

    def exists(self, value):
        pass

linked_list = myLinkedList()
linked_list.append(5)
linked_list.append(37)

print(linked_list.output())
linked_list.append(21)
print(linked_list.output())


# Reverse a singly linked list

def list_reverse(linkedlist):
    current = self.head
    prev = None
    while(current != None):
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
    
    return linkedlist