class TreeNode:
    def __init__(self,value):
        self.val = value
        self.Children = []
        self.ChildrenCount = 0


class Tree:
    def __init__(self, rootval):
        self.val = rootval
        self.Children = []
        self.ChildrenCount = 0


    def insertchild(self, value):
        Child = Tree(value)

        self.Children.append(Child)
        self.ChildrenCount += 1
        return Child


def BFS(node):
    BFSlist = []
    queue1 = [node]
    #print("At node",node.val, "with children ",node.Children)
    while queue1:
        #print("in while with queue", queue1)
        curNode = queue1[0]
        BFSlist.append(curNode.val)
        queue1=queue1[1:]
        for child in curNode.Children:
            queue1.append(child)
    return BFSlist



def DFS(node):
    DFSlist = []
    stack1 = [node]
    #print("At node",node.val, "with children ",node.Children)
    while stack1:
        #print("in while with queue", queue1)
        curNode = stack1[0]
        DFSlist.append(curNode.val)
        stack1=stack1[1:]
        for child in curNode.Children:
            stack1.insert(0, child)
    return DFSlist