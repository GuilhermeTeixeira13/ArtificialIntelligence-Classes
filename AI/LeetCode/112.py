# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, currSum):
            if not node:
                return False

            currSum += node.val
            if not node.right and not node.left:
                return currSum == targetSum

            return dfs(node.left, currSum) or dfs(node.right, currSum)

        return dfs(root, 0)


l = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().hasPathSum(l, 5))