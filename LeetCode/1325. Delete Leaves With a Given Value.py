# 1325. Delete Leaves With a Given Value
# [Problem Link](https://leetcode.com/problems/delete-leaves-with-a-given-value/submissions/1260677292?envType=daily-question&envId=2024-05-17)


# Overview

# Leetcode Problem 1325, "Delete Leaves With a Given Value," requires us to remove all leaf nodes from a binary tree that match a specific target value. A leaf node is defined as a node without children. The challenge is to ensure that the tree's structure is maintained correctly during this deletion process.

# Key Observations
#     1. **Leaf Nodes Deletion**: Deleting a leaf node can change its parent node into a new leaf node. Therefore, we must check and remove nodes from the bottom of the tree upwards.
#     2. **Tree Structure**: When a node is deleted, its parent's pointer needs to be updated to null, which can affect the entire tree structure.

# Approach: Recursion (Postorder Traversal)

# Intuition
#    Postorder traversal is suitable for this problem as it processes each node after its children, ensuring all descendant nodes are handled before their parent. This bottom-up approach efficiently deletes targeted nodes, capturing any new leaf nodes created by prior deletions.

# Algorithm
#     1. **Base Case**: If the root is null, return null (handles empty tree or end of branch).
#     2. **Recursive Traversal**:
#        - Recursively call `removeLeafNodes` for the left child.
#        - Recursively call `removeLeafNodes` for the right child.
#     3. **Node Evaluation**:
#        - Check if the current node is a leaf and its value equals the target. If true, return null to delete the node.
#        - Otherwise, return the current node.

# Implementation
# ```python

    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            """
            Initializes a binary tree node.
    
            Parameters:
            val (int): The value of the node.
            left (TreeNode): The left child node.
            right (TreeNode): The right child node.
            """
            self.val = val
            self.left = left
            self.right = right
    
    class Solution:
        def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            """
            Removes all leaf nodes with the given target value from the binary tree.
    
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
#     ```
#     Runtime 39 ms
#     Memory 17.0 MB
#     ```

# ### Real-World Example

# #### Scenario
# Consider managing a hierarchical organizational chart where employees are represented as nodes in a binary tree. Occasionally, employees (leaf nodes) leave the company and need to be removed from the chart.

# #### Initial Structure:
# ```
#        CEO
#       /   \
#     VP1    VP2
#    /  \   /  \
#  Mgr1 Mgr2 Mgr3 Mgr4
#  /
# Emp1
# ```
# #### Requirement
# Remove the leaf node "Emp1" who has left the company.

# #### Steps:
# 1. **Identify Target**: "Emp1".
# 2. **Apply Algorithm**:
#    - Traverse the tree to identify and remove "Emp1".

# #### Modified Structure:
# ```
#        CEO
#       /   \
#     VP1    VP2
#    /  \   /  \
#  Mgr1 Mgr2 Mgr3 Mgr4
# ```
# By removing "Emp1," the organizational chart maintains its structure without the former employee.

# ### Usage Examples and Test Cases

# #### Example 1:
# Input:
# ```python
# root = TreeNode(1, 
#                 TreeNode(2, TreeNode(2)), 
#                 TreeNode(3, TreeNode(2), TreeNode(4)))
# target = 2

# solution = Solution()
# result = solution.removeLeafNodes(root, target)
# ```

# Output:
# ```
#     1
#      \
#       3
#        \
#         4
# ```

# #### Example 2:
# Input:
# ```python
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# target = 2

# solution = Solution()
# result = solution.removeLeafNodes(root, target)
# ```

# Output:
# ```
#     1
#      \
#       3
# ```

# ### Complexity Analysis
#     #### Time Complexity
#         - **O(n)**: Each node in the binary tree is visited exactly once.
#         - Operations at each node (checking conditions, updating references) take constant time.
#     #### Space Complexity
#         - **O(n)**: In the worst-case scenario (unbalanced tree), the call stack can grow to the height of the tree, which equals the number of nodes.


# ### Conclusion
#     This solution effectively removes leaf nodes with the given target value using a recursive postorder traversal approach. The algorithm ensures that the tree's structure is maintained, and the solution is optimized for both time and space complexity. By following best practices in code documentation and structure, this solution is clear, maintainable, and accessible for future modifications and collaborations.

