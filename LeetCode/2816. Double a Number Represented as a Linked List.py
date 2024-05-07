# 2816. Double a Number Represented as a Linked List
# [Link problem] (https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/submissions/1251894336?envType=daily-question&envId=2024-05-07)


# **Overview:**
#     Problem 2816 tasks us with doubling a number represented as a linked list. We are given the head of a non-empty linked list representing a non-negative integer without leading zeroes. The goal is to return the head of the linked list after doubling the number it represents.

# **Approach:**
#     To solve this problem, we will reverse the linked list to simplify the number doubling process. Then, we will traverse the reversed linked list, doubling each digit while considering any carry-over from the previous digit. If there's a carry-over after doubling the last digit, we'll add a new node to accommodate it. Finally, we'll reverse the linked list again to restore its original order before returning the modified head.

# **Python3 Solution:**

#     ```python
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            """
            Initializes a node in a singly-linked list.
            
            Args:
                val (int): The value of the node.
                next (ListNode): Reference to the next node in the list.
            """
            self.val = val
            self.next = next
    
    
    class Solution:
        def reverseLinkedList(self, head: ListNode) -> ListNode:
            """
            Reverses a linked list in place.
            
            Args:
                head (ListNode): The head of the linked list to be reversed.
            
            Returns:
                ListNode: The head of the reversed linked list.
            """
            # Initialize pointers for the previous, current, and next nodes
            prev_node = None
            current_node = head
            
            # Traverse the linked list and reverse the pointers
            while current_node:
                # Store the next node to prevent losing its reference
                next_node = current_node.next
                
                # Reverse the pointer of the current node to point to the previous node
                current_node.next = prev_node
                
                # Move the pointers one step forward
                prev_node = current_node
                current_node = next_node
            
            # Return the new head of the reversed linked list
            return prev_node
    
        def doubleIt(self, head: ListNode) -> ListNode:
            """
            Doubles the number represented by a linked list.
            
            Args:
                head (ListNode): The head of the original linked list.
            
            Returns:
                ListNode: The head of the modified linked list representing the doubled number.
            """
            # Reverse the linked list to simplify number doubling
            head = self.reverseLinkedList(head)
            
            # Initialize the current node pointer and carry for addition
            current_node = head
            carry = 0
            
            # Iterate through the linked list to double each digit
            while current_node:
                # Double the current digit and add any carry-over from the previous digit
                current_node.val = current_node.val * 2 + carry
                
                # Calculate the carry-over for the next digit
                carry = current_node.val // 10
                
                # Update the current digit to be the remainder after division by 10
                current_node.val %= 10
                
                # If there's a carry after doubling the last digit, add a new node
                if carry and not current_node.next:
                    current_node.next = ListNode(carry)
                    break
                
                # Move to the next node in the linked list
                current_node = current_node.next
            
            # Reverse the linked list again to restore its original order
            head = self.reverseLinkedList(head)
            
            # Return the head of the modified linked list
            return head
#     ```
#         **Runtime:** 261 ms
#         **Memory:** 19.38 MB
#     ```

# **Annotations and Best Practices:**
#     - **Function and Variable Naming:** Descriptive names like `prev_node`, `current_node`, and `next_node` enhance readability.
#     - **Comments and Documentation:** Detailed docstrings explain the purpose and functionality of each function and method.
#     - **Code Structure and Organization:** The code is logically organized, with clear separation of concerns and consistent formatting.
#     - **Algorithm Explanation:** The algorithmic approach is outlined, highlighting the steps taken to double the number represented by the linked list.
#     - **Error Handling and Edge Cases:** Edge cases such as carry-over handling are addressed to ensure correct behavior in all scenarios.
#     - **Optimization and Performance:** The code minimizes unnecessary operations and efficiently reverses the linked list to optimize performance.
#     - **Usage Examples and Test Cases:** Usage examples and test cases are not provided within the solution but can be executed with sample data to verify correctness and functionality.

