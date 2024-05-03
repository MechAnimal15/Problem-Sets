# # **Portfolio Entry: Problem 165 - Compare Version Numbers**
# [Problem Link](https://leetcode.com/problems/compare-version-numbers/submissions/1248308832?envType=daily-question&envId=2024-05-03)

# ## **Problem Overview:**
# Problem 165 on LeetCode, "Compare Version Numbers," tasks us with comparing two version numbers represented as strings. The goal is to determine if one version is greater, lesser, or equal to the other. Version numbers consist of one or more revisions separated by dots ('.'). Each revision is a numeric value and may contain leading zeros. The comparison involves comparing revisions in left-to-right order, treating missing revisions as 0.

# ## **Approach:**
# To solve this problem, we split the version strings into lists of revisions and iterate through each revision to compare them numerically. We convert revisions to integers, defaulting to 0 for missing revisions. The algorithm iterates through both versions simultaneously, comparing revisions at corresponding indices. If one version has more revisions than the other, the missing revisions are treated as 0 during comparison.

# ## **Python3 Solution:**
# ```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compare two version numbers.
        
        Args:
            version1 (str): First version number string.
            version2 (str): Second version number string.
        
        Returns:
            int: -1 if version1 < version2, 1 if version1 > version2, 0 if equal.
        """
        # Split the version strings into lists of revisions.
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')
        
        # Determine the maximum number of revisions between the two versions.
        max_revisions = max(len(v1_revisions), len(v2_revisions))
        
        # Iterate through the revisions of both versions.
        for i in range(max_revisions):
            # Convert each revision to an integer or default to 0 if missing.
            v1_revision = int(v1_revisions[i]) if i < len(v1_revisions) else 0
            v2_revision = int(v2_revisions[i]) if i < len(v2_revisions) else 0
            
            # Compare revisions numerically.
            if v1_revision < v2_revision:
                return -1  # Return -1 if version1 < version2.
            elif v1_revision > v2_revision:
                return 1   # Return 1 if version1 > version2.
        
        # If all revisions are equal, return 0, indicating that both versions are the same.
        return 0
# ```
# Runtime: 42 ms
# Memory: 16.54 MB

# **Annotations and Best Practices:**
#      - Function and Variable Naming: Descriptive names such as v1_revisions, v2_revisions, max_revisions, and v1_revision enhance code readability by clearly indicating their purpose.
#     - Comments and Documentation: Inline comments explain the purpose of each code block and complex logic. The docstring for the compareVersion method provides a concise description of its functionality, parameters, and return value.
#     - Code Structure and Organization: The code is logically organized, with related functions grouped within the Solution class. Proper indentation and whitespace usage improve readability.
#     - Algorithm Explanation: The algorithm iterates through the revisions of both versions, comparing them numerically. This approach is chosen for its simplicity and efficiency in handling version numbers of varying lengths.
#     - Error Handling and Edge Cases: The code gracefully handles edge cases such as missing revisions and invalid input by treating missing revisions as 0 and ensuring integer conversion.
#     - Optimization and Performance: The algorithm has a time complexity of O(n), minimizing unnecessary comparisons for efficient execution.
#     - Usage Examples and Test Cases: Additional usage examples and test cases can be included to demonstrate the code's functionality and verify its correctness, promoting better understanding and collaboration among users.

