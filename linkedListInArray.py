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

    def reverse(self):
        prev = None
        crr = self.head
        while crr is not None:
            temp = crr.next
            crr.next = prev
            prev  = crr
            crr = temp
        self.head = prev
        return crr


    def printlist(self):
        node = self.head
        while node is not None:
            print(node.value)
            # arr.append(node.value)
            node =node.next
        
        # arr = []
        # node = self.head
        # while node is not None:
        #     arr.append(node.value)
        #     node =node.next
        # print(arr)

ll = Lnkedlist()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.reverse()
ll.printlist()


