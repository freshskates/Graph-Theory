from nodes.node import Node

class LinkedList(Node): 
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, data):
        if(not self.head):
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            self.tail.setNext(temp)
            self.tail = temp
    
    def remove(self, index: int):
        if(index == 0):
            garbage_collection = self.head
            self.head = self.head.getNext()
            del garbage_collection
            return 1

        i = index
        current = self.head
        while(current):        
            if(i - 1 == 0):
                garbage_collection = current.getNext()
                current.setNext(current.getNext().getNext())
                del garbage_collection
                break
            current = current.getNext()
            i -= 1
    
    def show(self):
        current = self.head
        while(current):        
            print("{} -> ".format(current.data), end="")
            current = current.getNext()
        print("null")

    def vectorize(self):
        output = []
        current = self.head
        while(current):        
            output.append(current.data)
            current = current.getNext()
        return output
    
    def __eq__(self, other):
        if(isinstance(other, LinkedList)):
            return self.vectorize() == other.vectorize()
        return False