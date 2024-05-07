# 2816. Double a Number Represented as a Linked List
# [Link problem] (https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/submissions/1251894336?envType=daily-question&envId=2024-05-07)


# '''
# Python3 solution
# '''

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

        current_node = head
        carry = 0

        # Iterate through the linked list to double each digit
        while current_node:
            current_node.val = current_node.val * 2 + carry
            carry = current_node.val // 10
            current_node.val %= 10

            # If there's a carry after doubling the last digit, add a new node
            if carry and not current_node.next:
                current_node.next = ListNode(carry)
                break

            current_node = current_node.next

        # Reverse the linked list again to restore its original order
        head = self.reverseLinkedList(head)

        return head


# '''
# Runitme: 261 ms
# Memory: 19.38
# '''

