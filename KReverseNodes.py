from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while True:
            # Check if there are at least k nodes left
            kth_node = self.get_kth_node(prev, k)
            if not kth_node:
                break
            next_group = kth_node.next
            
            # Reverse the group
            new_prev, new_head = self.reverse_group(prev.next, k)
            
            # Reconnect the links
            prev.next = new_head
            new_prev.next = next_group
            
            # Move prev to the new_prev for the next iteration
            prev = new_prev
        
        return dummy.next
    
    def get_kth_node(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
    
    def reverse_group(self, head, k):
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return (head, prev)
    
# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
    
# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Given input
input_list = [1, 2, 3, 4, 5]
k = 2

# Create the linked list
head = create_linked_list(input_list)

# Call the function
solution = Solution()
result_head = solution.reverseKGroup(head, k)

# Convert the result back to a list
result_list = linked_list_to_list(result_head)

print(result_list)  # Output: [2, 1, 4, 3, 5]