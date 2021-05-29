class Node: 
    def __init__(self, data = None):
        """
        Node Object Init
        any -> None
        """
        self.data = data
        self.next = None 
    
    def setData(self, data):
        self.data = data
        return 1        

    def setNext(self, next):
        if isinstance(next, Node):
            self.next = next
            return 1 
        return 0 
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def __repr__(self):
        data = "'{}'".format(self.data) if isinstance(self.data, str) else self.data
        return "Node({}, {})".format(data, self.next.data if self.next else None)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        return False

    def __ne__(self, other):
        if isinstance(other, Node):
            return self.data != other.data
        return False
    
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.data > other.data
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.data < other.data
        return False
