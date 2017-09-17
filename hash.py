# Number generated from a string or combination of strings
# JavaScript Objects use hashes 
# Collision: result of two keys hashing to same index
# Separate Chaining: when collision occurs--creates an array of linked list indices
# Aurora/Redis--use hash tables, companies store information user will need most quickly in hash tables (ie Facebook news feed)
# Downside of hash tables: memory heavy


# def my_hash(word):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return (alphabet.index(word[0]) (26) + alphabet.index(word[1])
    
# a = my_hash("adam")
# print(a)


class MyNode:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n

class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26
    
    def my_hash(self, key):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return alphabet.index(key[0])

    def insert(self, value):
        new_node = MyNode(self, value)
        key = self.my_hash(value)
        if self.buckets[key] != None:
            current = self.buckets[key]
            while current.value != None:
                if current.next == None:
                    current.next = new_node
                    return
                current = current.next
        else: 
            self.buckets[key] = new_node
            new_node.next = None 
            pass   
    
    def find(value):
        key = self.my_hash(self, value)
        if self.buckets[key] == None:
            return False

        else:
            head = self.buckets[key]
            while current.value != None:
                if current.value == value:
                    return True
                
                current = current.next
            return False

my_hash_table = MyHashTable()
my_hash_table.insert("aaron")
my_hash_table.insert("sarah")
my_hash_table.insert("jennifer")
print(my_hash_table.buckets)
my_hash_table.insert("james")
print(my_hash_table.buckets)
