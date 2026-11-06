# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import deque

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gain = {None: 0}          
        # best downward path sum starting at each node
        best = root.val
        stack = [(root, False)]

        while stack:
            node, children_done = stack.pop()
            if node is None:
                continue
            if not children_done:
                # 1st visit: come back to this node after its children
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                # 2nd visit: both children are already in `gain`
                l = max(gain[node.left], 0)    # drop negative branches
                r = max(gain[node.right], 0)
                best = max(best, node.val + l + r)   # path that bends at this node
                gain[node] = node.val + max(l, r)    # pass one branch up to the parent

        return best