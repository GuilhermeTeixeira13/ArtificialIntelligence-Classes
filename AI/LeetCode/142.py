# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        current = head

        while current:
            if current in visited:
                return current.val
            visited.add(current)
            current = current.next

        return None


l0 = ListNode(3)
l1 = ListNode(2)
l2 = ListNode(0)
l3 = ListNode(-4)

l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l1


print(Solution().detectCycle(l0).val)
