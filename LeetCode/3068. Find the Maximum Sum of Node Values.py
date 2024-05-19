3068. Find the Maximum Sum of Node Values
[Problem Link](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/submissions/1262278358?envType=daily-question&envId=2024-05-19)


Working solution. test case 1, 2,3. Not 4 (edge case).

Python3 solution:


from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """
        Finds the maximum possible sum of node values in a tree after performing XOR operations on node values.

        Args:
            nums (List[int]): A list of integers representing the values of nodes in the tree.
            k (int): An integer representing the value used in the XOR operation.
            edges (List[List[int]]): A list of lists representing the edges in the tree (not used in this solution).

        Returns:
            int: The maximum possible sum of node values after performing XOR operations.
        """

        # Initialize variables
        total_sum = 0  # Variable to store the total sum of node values
        count = 0  # Counter for the number of positive net changes
        positive_min = float("inf")  # Variable to store the minimum positive net change
        negative_max = float("-inf")  # Variable to store the maximum negative net change

        # Calculate net change for each node and update total sum
        for node_value in nums:
            # Calculate node value after the operation
            node_val_after_operation = node_value ^ k
            # Add original node value to the total sum
            total_sum += node_value
            # Calculate net change caused by the operation
            net_change = node_val_after_operation - node_value

            # Check if net change is positive
            if net_change > 0:
                # Update minimum positive net change
                positive_min = min(positive_min, net_change)
                # Update total sum by adding net change
                total_sum += net_change
                # Increment count of positive net changes
                count += 1
            else:
                # Update maximum negative net change
                negative_max = max(negative_max, net_change)

        # If count of positive net changes is even
        if count % 2 == 0:
            # Return the total sum
            return total_sum
        
        # If count of positive net changes is odd
        # Return the maximum sum considering both cases
        return max(total_sum - positive_min, total_sum + negative_max)

````
Runtime 
````
