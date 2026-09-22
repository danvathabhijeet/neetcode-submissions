# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = []
        sarea = deque([root])
        while sarea:
            level = []
            length = len(sarea)
            for _ in range(length):
                node = sarea.popleft()
                level.append(node.val)
                if node.left:
                    sarea.append(node.left)
                if node.right:
                    sarea.append(node.right)
            answer.append(level)
        return answer