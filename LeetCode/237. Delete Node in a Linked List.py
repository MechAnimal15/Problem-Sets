# 237. Delete Node in a Linked List
# [Problem Link](https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/1250181892?envType=daily-question&envId=2024-05-05)

# **Problem 237: Delete Node in a Linked List**

# **Problem Description:**
    # In this problem, we are given a singly-linked list with unique values and a node to be deleted. The task is to delete the given node from the linked list in-place. This deletion should remove the value of the given node from the list while maintaining the order of the remaining nodes.

# **Approach:**
    # The approach to solve this problem involves manipulating the pointers of the linked list to effectively remove the given node without altering the overall structure of the list. Instead of actually deleting the node, we copy the value of the next node to the current node, effectively "deleting" the current node by making it hold the value of the next node. Then, we update the next pointer of the current node to skip the next node, effectively removing it from the list.

                     
# **Python3 Solution:**
#     ```python
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.next = None
        
        class Solution:
            def deleteNode(self, node):
                """
                Deletes the given node from a singly-linked list in-place.
        
                :param node: The node to be deleted.
                :type node: ListNode
                :rtype: None
                """
               
                # Copy the value of the next node to the current node
                node.val = node.next.val
                
                # Update the next pointer of the current node to skip the next node
                node.next = node.next.next
        
#     '''
#     Python3 Solution: 
#     Runtime: 32 ms
#     Memory: 16.71 MB
#     ```


## Annotations and Best Practices:
#     - **Function and Variable Naming:**
#       - Descriptive names such as `deleteNode` for the method and `node` for the parameter enhance readability and clarity.
#     - **Comments and Documentation:**
#       - Inline comments explain each step of the algorithm, guiding readers through the purpose and logic of the code.
#       - A docstring is provided for the `deleteNode` method, describing its functionality and parameters.
#     - **Code Structure and Organization:**
#       - The code is logically organized within the `Solution` class, with proper indentation and whitespace usage for improved readability.
#     - **Algorithm Explanation:**
#       - An overview of the algorithm is provided, explaining the approach of copying the value of the next node and updating the pointers.
#     - **Error Handling and Edge Cases:**
#       - Since the problem guarantees that the given node is not the last node in the list, no explicit error handling is needed.
#     - **Optimization and Performance:**
#       - The solution achieves optimal performance by directly modifying the linked list without additional overhead.
#     - **Usage Examples and Test Cases:**
#       - Usage examples and test cases are not provided in the solution, but users can create their own linked lists and nodes for testing purposes.

## Conclusion:
# Overall, this Python3 solution for Problem 237 provides a clear and concise approach to deleting a node in a singly-linked list while adhering to best practices in coding standards and technical writing.


                     
