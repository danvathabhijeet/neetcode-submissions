# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = ""
        def encoder(node):
            nonlocal encoded
            if not node:
                encoded+=("Null,")
            else:
                encoded+=(str(node.val)+",")
                encoder(node.left)
                encoder(node.right)
        encoder(root)
        return encoded.rstrip(",")
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        count = 0
        def builder():
            nonlocal count
            val = values[count]
            count += 1
            if val == "Null":
                return None
            node = TreeNode(int(val))
            left = builder()
            right = builder()
            node.left = left 
            node.right = right 
            return node
        return builder()

