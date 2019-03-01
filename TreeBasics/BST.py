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


	#getting height of tree
    def TreeHeight(self):
        if self.root==None:
            return 0
        else:
            return self.SubTreeHeight(self.root,0)
    def SubTreeHeight(self,node, curHeight):
        if node==None:
            return curHeight
        leftHeight = self.SubTreeHeight(node.LChild,curHeight+1)
        rightHeight = self.SubTreeHeight(node.RChild,curHeight+1)
        return max(leftHeight,rightHeight)

    #search in the tree
    def searchValue(self,lookup):
        if self.root==None:
            return None
        else:
            return self.SubTreeSearch(self.root,lookup)
    
    def SubTreeSearch(self,node,lookup):
        if node==None:
            return False
        if node.val == lookup:
            return True
        elif node.val<lookup:
            return self.SubTreeSearch(node.RChild,lookup)
        else:
            return self.SubTreeSearch(node.LChild,lookup)

        return False
