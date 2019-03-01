from TreeBasics import node

class BST:
    def __init__(self):
        self.root =None
    

    def insert(self,value):
        if self.root is None:
            self.root = node.TreeNode(value)
        else:
            
            Child = node.TreeNode(value)
            self.insertInTree(self.root,Child)

    def insertInTree(self, parent,child):
        if child.val>parent.val :
            if parent.RChild==None:
                parent.RChild = child
            else:
                self.insertInTree(parent.RChild,child)
        else :
            if parent.LChild==None:
                parent.LChild = child
            else:
                self.insertInTree(parent.LChild,child)

    def printTree(self):
        if self.root==None:
            print("Empty Tree")
        else:
            self.printSubTree(self.root)
    def printSubTree(self,node):
        if node!=None:
            #inorder traversal
            #will give sorted order
            self.printSubTree(node.LChild)
            print(node.val)
            self.printSubTree(node.RChild)
        else:
            return    



