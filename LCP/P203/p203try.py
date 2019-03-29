# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        if not head:
            return None
        while head and  head.val == val:
            head = head.next
        if not head:
            return None
        p = head
        node= head.next
        while (node != None):
            
            if node.val == val:
                p.next = node.next
            else:
                p=node
            node = node.next
            
        return head
                
            

list1 = [1,2,6,3,4,5,6]
valie = 6


