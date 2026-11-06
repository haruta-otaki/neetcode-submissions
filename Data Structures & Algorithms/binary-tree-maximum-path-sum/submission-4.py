# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -sys.maxsize

        def helper(node):
            nonlocal best
            if node is None:
                return 0
            left_gain = max(helper(node.left), 0)    # 0 = "don't take this branch"
            right_gain = max(helper(node.right), 0)
            best = max(best, node.val + left_gain + right_gain)   # candidate answer
            return node.val + max(left_gain, right_gain)          # extendable path only

        helper(root)
        return best

