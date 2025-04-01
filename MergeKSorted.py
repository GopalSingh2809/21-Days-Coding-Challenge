import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        counter = 0  # To avoid comparing ListNode objects when values are equal
        
        # Insert the first node of each list into the heap
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1
        
        dummy = ListNode(0)
        current = dummy
        
        # Process the heap until it's empty
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next

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
input_lists = [[1,4,5],[1,3,4],[2,6]]

# Create linked lists from each sublist
linked_lists = []
for lst in input_lists:
    linked_lists.append(create_linked_list(lst))

# Call the function
solution = Solution()
result_head = solution.mergeKLists(linked_lists)

# Convert the result back to a list
result_list = linked_list_to_list(result_head)

print(result_list)  # Output: [1,1,2,3,4,4,5,6]