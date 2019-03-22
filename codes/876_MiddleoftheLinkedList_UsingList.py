# 876. Middle of the Linked List

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Traversal of the linked list to store every node into a new list, and return the middle one

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        ans = []
        while head:
            ans.append(head)
            head = head.next

        length = len(ans)
        return ans[length // 2]
