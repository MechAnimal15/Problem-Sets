1325. Delete Leaves With a Given Value
[Problem Link](https://leetcode.com/problems/delete-leaves-with-a-given-value/submissions/1260677292?envType=daily-question&envId=2024-05-17)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        This function removes all leaf nodes with the given target value from the binary tree.
        
        Parameters:
        root (TreeNode): The root of the binary tree.
        target (int): The target value for the leaf nodes to be removed.
        
        Returns:
        TreeNode: The root of the modified binary tree with target leaf nodes removed.
        """
        
        # Base case: If the current node is None, return None
        if not root:
            return None
        
        # Recursive step: Process the left subtree
        root.left = self.removeLeafNodes(root.left, target)
        
        # Recursive step: Process the right subtree
        root.right = self.removeLeafNodes(root.right, target)
        
        # Post-order traversal: Process the current node after its children
        
        # Check if the current node is a leaf and if its value matches the target
        if root.left is None and root.right is None and root.val == target:
            # If true, remove the current node by returning None
            return None
        
        # Return the current node (which may be modified or unchanged)
        return root

````
Runtime 39 ms
Memory 17.0 MB
````

