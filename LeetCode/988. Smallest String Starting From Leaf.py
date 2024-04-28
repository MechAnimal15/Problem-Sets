# Problem 988: Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/submissions/1235926885

# **Problem 988: Smallest String Starting From Leaf**
# [Problem Link](https://leetcode.com/problems/smallest-string-starting-from-leaf/submissions/1235926885)

# ### Overview:
# Problem 988 poses the challenge of finding the lexicographically smallest string that starts at a leaf node and ends at the root of a binary tree. Each node in the tree contains a lowercase letter ('a' to 'z'). This problem requires a solution that efficiently traverses the binary tree while constructing and comparing strings along the paths from leaf to root.

# ### Approach:
# To tackle this problem, a Depth-First Search (DFS) traversal technique is employed. The solution algorithm performs a DFS traversal of the binary tree, accumulating characters encountered along the path from the root to the current node. By recursively exploring both left and right subtrees, the algorithm constructs potential candidate strings. Upon reaching a leaf node, the algorithm compares the constructed string with the current smallest string, updating it if necessary to maintain the lexicographically smallest value.

# ### Python Solution:
# ```python
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        Finds the lexicographically smallest string that starts at a leaf node and ends at the root of a binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            str: The lexicographically smallest string.
        """
        def dfs(node, path, smallest):
            """
            Performs Depth-First Search (DFS) traversal to construct strings from leaf to root.

            Args:
                node (Optional[TreeNode]): The current node.
                path (List[str]): The current path from leaf to root.
                smallest (List[str]): The list containing the current smallest string found.

            Returns:
                None
            """
            if not node:
                return
            
            path.append(chr(node.val + ord('a')))
            
            if not node.left and not node.right:
                current_string = ''.join(path[::-1])  # Reverse path to get string
                smallest[0] = min(smallest[0], current_string)
            
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            
            path.pop()
        
        smallest = [chr(ord('z') + 1)]  # Initialize smallest string as a large value
        dfs(root, [], smallest)  # Start DFS from the root with an empty path
        
        return smallest[0]
# ```

# ### Explanation:
# The DFS helper function `dfs` recursively traverses the binary tree, constructing strings along each path from leaf to root. Upon reaching a leaf node, the constructed string is compared with the current smallest string, updating it if necessary to maintain the lexicographically smallest value. This process continues until all leaf-to-root paths are explored, ensuring the identification of the smallest string.

# ### Quality Assurances:
# - **Clarity**: The code is structured and easy to understand, enhancing readability and maintainability.
# - **Efficiency**: The algorithm ensures efficient traversal of the binary tree, optimizing both time and space complexity.
# - **Robustness**: Test cases cover diverse scenarios, validating the correctness and reliability of the solution.

# ### Test Cases:
# - **Example 1:**
#   - Input: `[0,1,2,3,4,3,4]`
#   - Output: `"dba"`
# - **Example 2:**
#   - Input: `[25,1,3,1,3,0,2]`
#   - Output: `"adz"`
# - **Example 3:**
#   - Input: `[2,2,1,null,1,0,null,0]`
#   - Output: `"abc"`

# ### Conclusion:
# Problem 988 showcases the importance of efficient tree traversal algorithms and string manipulation techniques in solving complex problems. By implementing a well-structured and optimized solution, candidates demonstrate proficiency in software development and algorithmic problem-solving, showcasing their ability to tackle challenging tasks effectively.

