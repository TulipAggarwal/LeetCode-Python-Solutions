#Approach-1: Using the approach of adding each index to the hashset and if the node in the hash set is being visited twice then we declare that there exists a 
#cycle and then display the index of the node we visit twice

#Approach-2: Using the floyd and tortoise's algorithm
-----------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
#Here take an example that the linked list is: 1->2->3->4 and then back at 2
#S    L
#1    1
#2    3
#3    2  -> we are using iteration to print the cycled node that is exactly before when slow and fast are going to be equal.
#4    4
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
