class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def nextNode(self, n):
        self.next = n
def partition(head,x):
    node = head
    smallerList = ListNode(0)
    smallhead = smallerList
    LargerList = ListNode(0)
    Largehead = LargerList
    while node != None :
        
        if node.val >=x:
            newnode = ListNode(node.val)
            LargerList.next = newnode
            LargerList = newnode
        else:
            newnode = ListNode(node.val)
            smallerList.next = newnode
            smallerList = newnode

        node= node.next
    
    node = smallhead.next
    print("smaller list")
    while node!=None:
        print(node.val)
        node = node.next
    print("Larger list")
    node = Largehead.next
    while node!=None:
        print(node.val)
        node = node.next
    
    
    print("Complete List")
    node = smallhead.next
    while node.next!=None:
        node = node.next
    node.next = Largehead.next
    
    node = smallhead.next
    while node!=None:
        print(node.val)
        node = node.next
    

l = [1,4,3,2,5,2]
h1 = ListNode(1)
print(h1,h1.next)
'''
for val in l:
    h2 = ListNode(val) 
    h1.next = h2
    h1=h2
'''
h2 = ListNode(4) 
h1.next = h2
h3 = ListNode(3) 
h2.next = h3
h4 = ListNode(2) 
h3.next = h4
h5 = ListNode(5) 
h4.next = h5
h6 = ListNode(2) 
h5.next = h6


print(partition(h1,3))
