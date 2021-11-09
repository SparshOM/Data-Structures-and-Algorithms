class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Lnkedlist:
    def __init__(self):
        self.head = None

    def insert(self,valueInsert):
        if self.head ==None:
            self.head =Node(valueInsert)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next=Node(valueInsert)

    def printlist(self):
        node = self.head
        while node is not None:
            print(node.value)
            node =node.next
ll = Lnkedlist()
ll.insert(1)
ll.insert(40)
ll.printlist()


