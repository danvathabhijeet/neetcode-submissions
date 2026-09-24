# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        count = 0
        def builder(left,right):
            nonlocal count
            if left > right:
                return None
            value = preorder[count]
            count+=1
            currentnode = hashmap[value]
            leftc = builder(left,currentnode-1)
            rightc = builder(currentnode+1,right)
            parent = TreeNode(value)
            parent.left = leftc
            parent.right = rightc
            return parent
        return builder(0,len(inorder) - 1)

        