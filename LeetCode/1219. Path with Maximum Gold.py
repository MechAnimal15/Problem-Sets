# 1219. Path with Maximum Gold
# [Problem Link](https://leetcode.com/problems/path-with-maximum-gold/submissions/1257977568?envType=daily-question&envId=2024-05-14)


# **Problem 1219: Path with Maximum Gold**

# **Overview:**
# In this problem, we are given a grid representing a gold mine, where each cell contains a certain amount of gold. The task is to find the maximum amount of gold that can be collected by starting from any cell containing gold and moving either up, down, left, or right to collect more gold.

# **Approach:**
# To solve this problem, we can utilize depth-first search (DFS) to explore all possible paths starting from each cell containing gold. We'll recursively traverse the grid, exploring all possible directions from each cell, while keeping track of the maximum amount of gold collected along the way. We'll mark visited cells to avoid revisiting them and backtrack once we've exhausted all possible paths from a cell.

# **Python Solution:**
#     ```python
    
        from typing import List
        
        class Solution:
            def getMaximumGold(self, grid: List[List[int]]) -> int:
                """
                Finds the maximum amount of gold that can be collected from the gold mine grid.
        
                Args:
                    grid (List[List[int]]): The grid representing the gold mine, where each cell contains the amount of gold.
        
                Returns:
                    int: The maximum amount of gold that can be collected.
                """
        
                def dfs(row: int, col: int) -> int:
                    """
                    Performs depth-first search (DFS) to explore all possible paths from a given cell.
        
                    Args:
                        row (int): The row index of the current cell.
                        col (int): The column index of the current cell.
        
                    Returns:
                        int: The maximum amount of gold that can be collected starting from the current cell.
                    """
                    # Base case: check if the current cell is valid or contains gold
                    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                        return 0
        
                    # Temporarily mark the current cell as visited by setting its value to 0
                    gold_collected = grid[row][col]
                    grid[row][col] = 0
        
                    # Explore all four directions (up, down, left, right) from the current cell
                    max_gold = max(
                        dfs(row + 1, col),
                        dfs(row - 1, col),
                        dfs(row, col + 1),
                        dfs(row, col - 1),
                    )
        
                    # Restore the original value of the current cell after DFS traversal
                    grid[row][col] = gold_collected
        
                    return max_gold + gold_collected
        
                # Initialize the maximum gold collected to 0
                max_gold_collected = 0
        
                # Iterate through each cell in the grid
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        # If the current cell contains gold, perform DFS to find the maximum gold that can be collected
                        if grid[i][j] != 0:
                            max_gold_collected = max(max_gold_collected, dfs(i, j))
        
                return max_gold_collected
        
#     ```
#     1219. Path with Maximum Gold
#         Runtime: 2186 ms
#         Memory: 16.3 MB   
#     ```

# **Key Aspects:**
#     1. **Function and Variable Naming:** Descriptive names like `dfs` for depth-first search function and `max_gold_collected` for tracking maximum gold collected enhance code readability.
#     2. **Comments and Documentation:** Comprehensive docstrings provide clear descriptions of the purpose, parameters, and return values of functions, improving code understanding.
#     3. **Code Structure and Organization:** The code is logically organized into functions, with related functionality grouped together. Consistent whitespace and indentation enhance readability.
#     4. **Algorithm Explanation:** Depth-first search is chosen due to its suitability for exploring all possible paths. The algorithm recursively traverses the grid, backtracking when necessary, to find the maximum gold.
#     5. **Error Handling and Edge Cases:** Base cases handle invalid cells or cells with no gold. Comments guide error handling and ensure graceful behavior.
#     6. **Optimization and Performance:** While no specific optimizations are implemented, the solution efficiently explores all paths to find the maximum gold.
#     7. **Usage Examples and Test Cases:** Sample inputs and expected outputs can be provided to validate the correctness of the solution. For example:


#     ```python
#         solution = Solution()
#         grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
#         print(solution.getMaximumGold(grid))  # Output: 24
#     ```

# **Conclusion:**
#     The provided solution effectively solves Problem 1219, "Path with Maximum Gold," using depth-first search to explore all possible paths in the gold mine grid. The code is well-documented, organized, and optimized for readability and efficiency, making it suitable for both technical and non-technical audiences.

