from TreeBasics import BST
#from TreeBasics import node
from TreeBasics import NormalTree


T1 = NormalTree.Tree(74)
lsit = [56,76,3,22,96,324,5,32,94]
r1 = T1.insertchild(56)
l1 = T1.insertchild(76)

r11 = r1.insertchild(3)
r12 = r1.insertchild(22)
r13 = r1.insertchild(96)

l11 = l1.insertchild(324)
l12 = l1.insertchild(5)
l13 = l1.insertchild(32)

#T1.printTree()
print("Children of 56",r1.ChildrenCount)
for i in r1.Children:
    print(i.val)

print("BFS list is : ",NormalTree.BFS(T1))

print("DFS list is : ",NormalTree.DFS(T1))