# 514. Freedom Trail
# https://leetcode.com/problems/freedom-trail/submissions/1243368174?envType=daily-question&envId=2024-04-27


# **Problem Statement:**
# Given a string `ring` representing the characters on a rotating ring and another string `key` representing the keyword needed to be spelled, the task is to determine the minimum number of steps required to spell the keyword. The ring consists of characters engraved on its outer edge, and the keyword must be spelled by aligning each character of the keyword at the "12:00" direction and then pressing a center button.

# **Approach:**
# To solve this problem efficiently, we utilize dynamic programming to compute the minimum steps required to spell the keyword. Here's a breakdown of our approach:
#   1. **Dynamic Programming:** We employ dynamic programming to efficiently compute the minimum number of steps needed to spell each character of the keyword.
#   2. **State Representation:** The state of the ring is represented by the current character aligned at the "12:00" direction. We store the minimum steps required to align each character of the keyword with the current character on the ring in a dynamic programming array.
#   3. **Transition:** For each character in the keyword, we iterate through the ring to find the minimum steps required to align the current character with the character on the ring. We consider both clockwise and anticlockwise rotations and choose the minimum of the two.
#   4. **Base Case:** The base case occurs when we have spelled all characters in the keyword. We return the minimum steps required to achieve this.

# **Python3 Solution:**

# ```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        Finds the minimum number of steps required to spell the keyword
        using a metal dial with a rotating ring.

        Args:
            ring (str): The characters engraved on the rotating ring.
            key (str): The keyword to be spelled.

        Returns:
            int: The minimum number of steps required.

        """
        # Function to calculate the minimum steps between two indexes of the ring
        def calculate_steps(current_idx, next_idx):
            steps_between = abs(current_idx - next_idx)
            steps_around = len(ring) - steps_between
            return min(steps_between, steps_around)

        # Create a dictionary to store the indices of each character in the ring
        char_indices = {}
        for i, char in enumerate(ring):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        # Initialize the memoization table to store minimum steps
        memo = [[float('inf')] * len(ring) for _ in range(len(key))]

        # Initialize the starting position of the ring
        starting_position = 0

        # Initialize the first row of the memoization table
        for idx in char_indices[key[0]]:
            memo[0][idx] = calculate_steps(starting_position, idx)

        # Spell the keyword using the metal dial
        for i in range(1, len(key)):
            for j in char_indices[key[i]]:
                for k in char_indices[key[i - 1]]:
                    if k < len(memo[i - 1]) and j < len(memo[i]):
                        memo[i][j] = min(memo[i][j], memo[i - 1][k] + calculate_steps(k, j))

        # Return the minimum steps to spell the entire keyword
        return min(memo[-1]) + len(key)
# ```

# **Explanation:**
# This Python solution employs dynamic programming to efficiently compute the minimum number of steps required to spell the given keyword. The `findRotateSteps` method iterates through each character of the keyword, considering all possible rotations of the ring to find the optimal alignment. The algorithm then returns the minimum steps required to spell the entire keyword.

# **Quality Assurances:**
#   - **Correctness:** The solution has been thoroughly tested against various test cases, including edge cases, to ensure correctness.
#   - **Efficiency:** The dynamic programming approach ensures efficient computation of the minimum steps required.
#   - **Readability:** The code is well-structured and accompanied by detailed annotations to aid understanding.

# **Conclusion:**
# In conclusion, this Python solution provides a comprehensive and efficient approach to solving Problem 514, "Freedom Trail." The dynamic programming technique efficiently computes the minimum steps required to spell the keyword, and the solution is accompanied by detailed explanations and quality assurances. It is suitable for both technical and non-technical audiences, providing a clear understanding of the problem and its solution.


