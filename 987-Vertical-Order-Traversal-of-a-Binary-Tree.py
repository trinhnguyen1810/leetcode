from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = []  # Stores (x, y, val)
        res = defaultdict(list)

        def dfs(node, x, y):
            if not node:
                return
            nodes.append((x, y, node.val))  # Store node value instead of object
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)

        # Sort by (column x, row y, node val)
        nodes.sort(key=lambda t: (t[0], t[1], t[2]))

        for x, y, val in nodes:
            res[x].append(val)

        return [res[key] for key in sorted(res)]
