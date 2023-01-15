# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        while curr:
            # Save next
            nxt = curr.next

            # Invert Pointer
            curr.next = prev

            # Shift pointers
            prev = curr
            curr = nxt

        return prev

print(Solution().reverseList(int(input())))