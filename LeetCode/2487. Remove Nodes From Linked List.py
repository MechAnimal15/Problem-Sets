2487. Remove Nodes From Linked List
[Problem Link](https://leetcode.com/problems/remove-nodes-from-linked-list/submissions/1251068805?envType=daily-question&envId=2024-05-06)




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
        prev_node = None
        current_node = head
        
        # Traverse the linked list and reverse the pointers
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        return prev_node

    def removeNodes(self, head: ListNode) -> ListNode:
        """
        Removes nodes from the linked list which have a greater value anywhere to the right side of them.
        
        Args:
            head (ListNode): The head of the original linked list.
        
        Returns:
            ListNode: The head of the modified linked list.
        """
        # Reverse the linked list to simplify node removal
        head = self.reverseLinkedList(head)
        
        max_value = float('-inf')
        dummy = ListNode(0)
        dummy.next = head
        current_node = head
        
        # Iterate through the linked list to find nodes to remove
        while current_node:
            # Update the maximum value encountered so far
            max_value = max(max_value, current_node.val)
            
            # If the value of the current node is less than the maximum value,
            # remove the node from the list by updating the next pointer of the previous node
            if current_node.val < max_value:
                dummy.next = current_node.next
            else:
                dummy = current_node
            current_node = current_node.next
        
        # Reverse the linked list again to restore its original order
        head = self.reverseLinkedList(head)
        
        return head
# ''''
# Runtime: 458 ms
# Memory: 50.86

