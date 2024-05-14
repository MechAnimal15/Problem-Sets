1219. Path with Maximum Gold
[Problem Link](https://leetcode.com/problems/path-with-maximum-gold/submissions/1257977568?envType=daily-question&envId=2024-05-14)


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
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 0
            ):
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

  """
  Runtime: 2251 ms
  Memory: 16.5 MB   
  """

