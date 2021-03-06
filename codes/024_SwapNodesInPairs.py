# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Explanation : In order to avoid to modify the value, I have used a previous node, which the next node of the 
# current node will be inserted between the previous node and current node.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            nextNode = curr.next
            if nextNode:
                curr.next = curr.next.next
                prev.next = nextNode
                nextNode.next = curr
            else:
                break
            prev = curr
            curr = curr.next

        return dummy.next
