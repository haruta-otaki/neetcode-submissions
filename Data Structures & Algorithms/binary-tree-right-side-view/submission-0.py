# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS and return the singular value on the one on the right most side 
        output = []
        queue = deque()
        if root is not None: 
            queue.append(root)
        while len(queue) > 0:
            current_neighbors = list(queue)
            node = queue.popleft()
            output.append(node.val)
            queue.clear()
            for node in current_neighbors: 
                if node.right is not None: 
                    queue.append(node.right)
                if node.left is not None: 
                    queue.append(node.left)
        return output