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
    # def inorder(self):
        
    #     if self.left:
    #         self.left.inorder()
    #     print( self.value)
    #     if self.right:
    #         self.right.inorder()

    # def preorder(self):
        
    #     print(self.value)
    #     if self.left:
    #         self.left.preorder()
    #     if self.right:
    #         self.right.preorder()
    
            
    # def postorder(self):
    #     if self.left:
    #         self.left.postorder()
    #     if self.right:
    #         self.right.postorder()
    #     print(self.value)

    def Search(self,target):
        crrnode = self
        if crrnode.value<target:
            crrnode = crrnode.right
        elif crrnode.value>target:
            crrnode = crrnode.left
        print(crrnode.value ==target)

root= bst(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(1)
root.insert(12)
root.insert(14)
root.insert(75)
# root.inorder()
# root.preorder()
# root.postorder()
root.Search(10)