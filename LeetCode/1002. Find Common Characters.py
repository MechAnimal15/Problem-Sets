# 1002. Find Common Characters
# [Problem Link](https://leetcode.com/problems/find-common-characters/submissions/1278632607?envType=daily-question&envId=2024-06-05)


# Overview
#     This portfolio entry provides a detailed overview of the solution to Leetcode Problem 1002, "Find Common Characters." The problem requires finding all characters that appear in all strings within an array of strings, including duplicates. The solution utilizes an efficient approach to track character frequencies and determine common characters across multiple strings. This entry includes a comprehensive explanation of the approach, a well-documented Python3 solution, and insights into error handling, optimization, and usage examples.
    
# Problem Statement
#     Given a string array `words`, return an array of all characters that show up in all strings within the `words` (including duplicates). You may return the answer in any order.

#  Example 1:
#     - **Input:** `words = ["bella", "label", "roller"]`
#     - **Output:** `["e", "l", "l"]`

#  Example 2:
#     - **Input:** `words = ["cool", "lock", "cook"]`
#     - **Output:** `["c", "o"]`

#  Constraints:
#     - `1 <= words.length <= 100`
#     - `1 <= words[i].length <= 100`
#     - `words[i]` consists of lowercase English letters.

# Approach: Array + Frequency Intersection

# Intuition
#     To solve the problem of finding common characters in multiple strings, we need to track the frequencies of each character in every string and determine the minimum frequency for each character that appears in all strings. By doing so, we ensure that the characters are present in all strings and are returned the correct number of times.

# Algorithm
#     1. **Initialization**:
#        - Create a frequency array `common_count` of size 26 (for each letter of the alphabet), initialized to the frequencies of the characters in the first word.
    
#     2. **Iterate Through the Words**:
#        - For each subsequent word, create a `current_count` array to track character frequencies.
#        - Update `common_count` by taking the minimum frequency of each character between `common_count` and `current_count`.
    
#     3. **Collect Common Characters**:
#        - Iterate over `common_count` and construct the result list based on the frequencies stored in `common_count`.

# Complexity Analysis
#     - **Time Complexity**: \(O(n \cdot k)\), where \(n\) is the number of words and \(k\) is the length of the longest word. This accounts for iterating through each word and updating the frequency counts.
#     - **Space Complexity**: \(O(1)\), as the frequency arrays `common_count` and `current_count` are fixed in size (26).

# Python3 Solution
#     Below is the Python3 solution with detailed annotations and documentation:

# ```python
    from typing import List
    
    class Solution:
        def commonChars(self, words: List[str]) -> List[str]:
            """
            Finds all characters that appear in all strings within the input list of words,
            including duplicates. Returns the common characters in any order.
            
            Parameters:
            words (List[str]): List of strings consisting of lowercase English letters.
            
            Returns:
            List[str]: List of characters that are common in all strings.
            """
            
            # Initialize the frequency array for the first word
            # Each index represents a letter in the alphabet ('a' = 0, 'z' = 25)
            common_count = [0] * 26
            base_word = words[0]
    
            # Populate the initial frequency count based on the first word
            for char in base_word:
                common_count[ord(char) - ord('a')] += 1
            
            # Update the frequency count based on the remaining words
            for word in words[1:]:
                # Temporary frequency array for the current word
                current_count = [0] * 26
                for char in word:
                    current_count[ord(char) - ord('a')] += 1
                
                # Update common_count to reflect the minimum frequency for each character
                for i in range(26):
                    common_count[i] = min(common_count[i], current_count[i])
            
            # Collect the common characters based on the frequency count
            result = []
            for i in range(26):
                result.extend([chr(i + ord('a'))] * common_count[i])
            
            return result
    
    # Usage examples and test cases
    solution = Solution()
    
    # Example 1
    words1 = ["bella", "label", "roller"]
    print(solution.commonChars(words1))  # Output: ["e", "l", "l"]
    
    # Example 2
    words2 = ["cool", "lock", "cook"]
    print(solution.commonChars(words2))  # Output: ["c", "o"]
```

# Detailed Annotations and Documentation

#     1. **Function and Variable Naming**:
#        - The function `commonChars` clearly indicates that it finds common characters.
#        - Variables like `common_count`, `current_count`, and `base_word` are named descriptively to reflect their roles.
    
#     2. **Comments and Documentation**:
#        - Each step of the algorithm is explained with comments.
#        - The function includes a docstring describing its purpose, parameters, and return value.
    
#     3. **Code Structure and Organization**:
#        - The code is organized logically, with clear separation between initialization, frequency updates, and result collection.
#        - Consistent indentation and spacing are used to enhance readability.
    
#     4. **Algorithm Explanation**:
#        - The algorithm initializes `common_count` with frequencies from the first word.
#        - For each subsequent word, it updates `common_count` to reflect the minimum frequencies.
#        - The result is constructed by collecting characters based on the final `common_count`.
    
#     5. **Error Handling and Edge Cases**:
#        - The code assumes valid input as per problem constraints (non-empty list of lowercase English words).
#        - Potential edge cases, such as single-word input, are inherently handled by the algorithm.
    
#     6. **Optimization and Performance**:
#        - The algorithm efficiently uses fixed-size arrays for frequency counting.
#        - By updating `common_count` with minimum frequencies, the solution ensures optimal performance.
    
#     7. **Usage Examples and Test Cases**:
#        - Examples demonstrate how the code should be used and verify its correctness.
#        - Sample inputs and expected outputs are provided to illustrate the expected behavior.

# Conclusion
#     This solution efficiently finds common characters in an array of strings using frequency counting and intersection. The detailed annotations and documentation enhance readability and understanding, catering to both technical and non-technical audiences. By following best practices in function naming, commenting, and code organization, this solution serves as a robust and maintainable approach to solving the problem.

