# 206. Reverse Linked List

# Reverse a singly linked list.

# Explanation : in order to reverse the single linked list, only thing we need to do is to reverse the next direction.
# means we change the next pointer of the current node to the previous node. Like we cut the node connection between the currrent
# node and the current.next node, but exchange the connection from current node to previous node. and then shift the previous to 
# current, and the current to NextNode.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
