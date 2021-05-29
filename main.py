# from Nodes.node import Node
from linked_list.linkedlist import LinkedList

def main():
    list_node = LinkedList()
    list_node.add("data")
    list_node.add("data1")
    list_node.add("data2")
    list_node.add("data3")
    list_node.show()
    print(list_node.vectorize())
    list_node.remove(1)
    list_node.remove(0)
    list_node.remove(0)
    list_node.show()


if __name__ == '__main__':
    main()