##19. Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.

## Solution
# This is an classic two pointer problem, which we need two pointer the distance of the two pointer
# should be the given n. and we traverse the linked list until the faster pointer get to end, and
# remove the node at the slow index.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy
        while n != 0:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
