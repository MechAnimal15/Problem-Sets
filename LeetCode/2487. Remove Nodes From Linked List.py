class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def removeNodes(self, head: ListNode) -> ListNode:
        # Reverse the linked list
        head = self.reverseLinkedList(head)
        
        max_value = float('-inf')
        dummy = ListNode(0)
        dummy.next = head
        current = head
        
        # Iterate through the linked list
        while current:
            # Update the maximum value
            max_value = max(max_value, current.val)
            
            # If the value of the current node is less than the maximum value,
            # keep the current node in the list by updating the next pointer of the previous node
            if current.val < max_value:
                dummy.next = current.next
            else:
                dummy = current
            current = current.next
        
        # Reverse the linked list again to restore its original order
        head = self.reverseLinkedList(head)
        
        return head
