# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        cal1 = l1
        cal2 = l2
        length1 = 0
        length2 = 0
        while cal1:
            length1 += 1
            cal1 = cal1.next
        while cal2:
            length2 += 1
            cal2 = cal2.next

        if length1 >= length2:
            node1 = l1
            node2 = l2
            count = 0
            while node1 or node2:
                if node1 and node2:
                    if node1.val + node2.val + count < 10:
                        node1.val = node1.val + node2.val + count
                        count = 0
                    else:
                        node1.val = node1.val + node2.val - 10 + count
                        count = 1

                    if node1.next:
                        node1 = node1.next
                        node2 = node2.next
                    else:
                        if count == 1:
                            node1.next = ListNode(count)
                        break

                    if node1 != None and node2 == None:
                        node2 = ListNode(0)

            return l1
        if length1 < length2:
            node1 = l2
            node2 = l1
            count = 0
            while node1 or node2:
                if node1 and node2:
                    if node1.val + node2.val + count < 10:
                        node1.val = node1.val + node2.val + count
                        count = 0
                    else:
                        node1.val = node1.val + node2.val - 10 + count
                        count = 1

                    if node1.next:
                        node1 = node1.next
                        node2 = node2.next
                    else:
                        if count == 1:
                            node1.next = ListNode(count)
                        break

                    if node1 != None and node2 == None:
                        node2 = ListNode(0)

            return l2
