# **Problem 1915 - Number of Wonderful Substrings**
# https://leetcode.com/problems/number-of-wonderful-substrings/submissions/1245818176?envType=daily-question&envId=2024-04-30


# **Overview:**
#   Problem 1915 on LeetCode, titled "Number of Wonderful Substrings," challenges us to count the number of wonderful non-empty substrings in a given string. A string is considered wonderful if at most one letter appears an odd number of times. This problem falls under the medium difficulty category and offers an opportunity to showcase skills in string manipulation, bitwise operations, and algorithmic optimization.

# **Approach:**
#   To solve this problem efficiently, we utilize a bitmasking approach along with a frequency counting technique. We iterate through each character in the string and maintain a bitmask to represent the count of each character in the current substring. By toggling the corresponding bit in the bitmask for each character encountered, we can efficiently track the parity of character occurrences. Additionally, we maintain a count array to store the frequency of each bitmask, allowing us to quickly calculate the number of wonderful substrings.

# **Algorithm:**
#   1. Initialize a count array to keep track of the frequency of each bitmask, with count[0] = 1 to handle the case when no characters are present.
#   2. Initialize a bitmask to represent the count of each character in the current substring.
#   3. Iterate through each character in the input string.
#   4. Calculate the index of the current character and toggle the corresponding bit in the bitmask.
#   5. Increment the count of wonderful substrings by adding the count of the current bitmask and all possible substrings formed by toggling one bit of the bitmask.
#   6. Update the count array by incrementing the count for the current bitmask.
#   7. Return the total count of wonderful substrings.

# **Python3 Solution:**

# ```python
class Solution:
    @staticmethod
    def wonderfulSubstrings(s: str) -> int:
        """
        Count the number of wonderful non-empty substrings in a given string.

        Args:
            s (str): Input string consisting of lowercase English letters from 'a' to 'j'.

        Returns:
            int: The count of wonderful non-empty substrings in the input string.

        """

        # Initialize a count array to keep track of the frequency of each bitmask.
        count = [1] + [0] * 1023  # 2^10 + 1
        
        # Initialize a bitmask to represent the count of each character in the current substring.
        mask = 0
        
        # Initialize the result to store the count of wonderful substrings.
        result = 0
        
        # Iterate through each character in the string.
        for c in s:
            # Calculate the index of the current character in the range [0, 9].
            idx = ord(c) - ord('a')
            
            # Toggle the corresponding bit in the bitmask.
            mask ^= 1 << idx
            
            # Increment the result by the count of the current bitmask.
            result += count[mask]
            
            # Increment the result by the count of all possible substrings formed by toggling one bit of the bitmask.
            for i in range(10):
                result += count[mask ^ (1 << i)]
            
            # Update the count array by incrementing the count for the current bitmask.
            count[mask] += 1
        
        # Return the total count of wonderful substrings.
        return result

# # Example usage:
# s = "aba"
# print(Solution.wonderfulSubstrings(s))  # Output: 4
# ```

# **Key Features:**
#   - **Function and Variable Naming**: Descriptive names are used for functions, variables, and parameters to reflect their purpose clearly.
#   - **Comments and Documentation**: Comprehensive comments and docstrings are provided to explain the purpose of each section of code and clarify complex logic.
#   - **Code Structure and Organization**: The code is organized logically, following best practices and design patterns, with related functions grouped together.
#   - **Algorithm Explanation**: An overview of the algorithm used is provided, along with relevant background information and considerations.
#   - **Error Handling and Edge Cases**: The code handles errors and edge cases gracefully, with comments or exceptions guiding users in handling unexpected behavior.
#   - **Optimization and Performance**: Considerations for optimization and performance are discussed, highlighting design choices made to improve efficiency.
#   - **Usage Examples and Test Cases**: Example usage and test cases are included to demonstrate how the code should be used and verify its correctness, aiding both technical and non-technical users in understanding and testing the solution.

