# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []

        def dfs(node):
            if not node: return
            output.append(node.val)
            for c in node.children:
                dfs(c)

        dfs(root)

        return output