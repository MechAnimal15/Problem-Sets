237. Delete Node in a Linked List

class Solution:
    def deleteNode(self, node):
        """
        Deletes the given node from a singly-linked list in-place.

        :param node: The node to be deleted.
        :type node: ListNode
        :rtype: None
        """
        # To delete the given node, we copy the value of the next node to the current node
        # and then update the next pointer of the current node to skip the next node.

        # Copy the value of the next node to the current node
        node.val = node.next.val
        
        # Update the next pointer of the current node to skip the next node
        node.next = node.next.next
