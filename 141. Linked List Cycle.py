#Approach-1: Using the approach of adding each index to the hashset and if the node in the hash set is being visited twice then we declare that there 
#exists a cycle and then display the index of the node we visit twice.

#Approach-2: Using the floyd and tortoise's algorithm.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#In this problem we have used the approach-1.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
