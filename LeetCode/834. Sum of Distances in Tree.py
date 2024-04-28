# **Problem 834 - Sum of Distances in Tree**
# https://leetcode.com/problems/sum-of-distances-in-tree/submissions/1244283563?envType=daily-question&envId=2024-04-28


# **Problem Description:**

# There is an undirected connected tree with \( n \) nodes labeled from 0 to \( n - 1 \) and \( n - 1 \) edges. You are given the integer \( n \) and the array \( edges \) where \( edges[i] = [a_i, b_i] \) indicates that there is an edge between nodes \( a_i \) and \( b_i \) in the tree. Return an array \( answer \) of length \( n \) where \( answer[i] \) is the sum of the distances between the \( i \)th node in the tree and all other nodes.

# ---

# **Approach:**

# - **Constructing the Adjacency List:**
#     - We begin by constructing an adjacency list to represent the graph structure of the tree. This allows us to efficiently traverse the tree.

# - **Performing Two DFS (Depth-First Search) Traversals:**
#     - We perform two DFS traversals to calculate the sum of distances from each node to all other nodes in the tree.
#     - In the first DFS traversal, we calculate the number of nodes in the subtree rooted at each node and the sum of distances from each node to its children.
#     - In the second DFS traversal, we update the sum of distances for each node based on the values calculated in the first traversal.

# ---

# **Python Solution:**

# ```python
from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Calculates the sum of distances from each node to all other nodes in an undirected connected tree.

        Args:
            n (int): The number of nodes in the tree.
            edges (List[List[int]]): The list of edges representing connections between nodes.

        Returns:
            List[int]: The list of sums of distances for each node.

        Algorithm:
            1. Construct Adjacency List:
                - Create an adjacency list to represent the graph structure of the tree.
            2. Perform Two DFS:
                - Perform two Depth-First Searches (DFS) to calculate the sum of distances from each node to all other nodes.

        Complexity Analysis:
            - Time Complexity: O(N), where N is the number of nodes in the tree.
            - Space Complexity: O(N), where N is the number of nodes in the tree.
        """

        # Step 1: Construct adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Perform two DFS to calculate sum of distances
        count = [1] * n  # Number of nodes in subtree rooted at each node
        result = [0] * n  # Sum of distances from each node to all other nodes

        def dfs1(node, parent):
            """Perform the first DFS traversal."""
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    count[node] += count[neighbor]
                    result[node] += result[neighbor] + count[neighbor]

        def dfs2(node, parent):
            """Perform the second DFS traversal."""
            for neighbor in graph[node]:
                if neighbor != parent:
                    result[neighbor] = result[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)

        dfs1(0, -1)  # Start DFS from the root (node 0)
        dfs2(0, -1)  # Start second DFS from the root (node 0)

        return result

# # Test the solution
# solution = Solution()
# n = 6
# edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# print(solution.sumOfDistancesInTree(n, edges))
# ```

# ---

# **Conclusion:**

# The solution effectively calculates the sum of distances from each node to all other nodes in an undirected connected tree using a combination of adjacency list representation and two DFS traversals. The algorithm has a time complexity of \( O(N) \) and a space complexity of \( O(N) \), making it efficient for trees with a large number of nodes.

# This portfolio entry provides a comprehensive overview of Problem 834 - Sum of Distances in Tree, covering the problem description, approach, Python solution, and conclusion. The approach section explains the algorithm used, and the Python solution is annotated to enhance readability and understanding. Additionally, complexity analysis is provided to give insights into the efficiency of the solution. Overall, this portfolio entry offers a detailed explanation of the problem and its solution, catering to both technical and non-technical audiences.

