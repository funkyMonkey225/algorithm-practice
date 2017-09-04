#Last in first out


class Node:
    def __init__(self, value, below=None):
        self.value = value
        self.below = below

class MyStack:
    def __init__(self):
        self.top = None
    
    def peek(self):
        return self.top
    
    def pop(self):
        if self.top == None:
            return None

        node_to_return = self.top
        self.top = self.top.below
        return node_to_return

    
    def push(self, value):
        new_node = Node(value)
        new_node.below = self.top
        self.top = new_node
        


stacky = MyStack()
stacky.push("ham")
print(str(stacky.peek()))
stacky.push("bacon")
print(str(stacky.peek()))
stacky.push("green eggs")
print(str(stacky.peek()))