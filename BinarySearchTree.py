class bst:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None
    def insert(self,value):    
        crrNode= self
        while True:
            if value<crrNode.value:
                if crrNode.left is None:
                    crrNode.left=bst(value)
                    break
                else:
                    crrNode = crrNode.left
            else:
                if crrNode.right is None:
                    crrNode.right = bst(value)
                    break
                else:
                    crrNode =crrNode.right
        return self
root= bst(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(22)