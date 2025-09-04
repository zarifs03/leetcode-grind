# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time complexity: O(n)
# Space complexity: O(1)

        # Alternative approach: copy linked list elements to an array and divide len(arr) by 2
        # arr = []

        # while head:
        #     arr.append(head)
        #     head = head.next
        
        # length = len(arr)
        # return arr[length // 2] # floor division required for indexing

# Time complexity: O(n)
# Space complexity: O(n) 

