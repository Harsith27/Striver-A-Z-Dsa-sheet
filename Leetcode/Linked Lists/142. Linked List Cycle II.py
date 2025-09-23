# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break               #1.normal cycle detection
        else:
            return None
        fast=head                   #2.set fast to head
        while(slow!=fast):          #3.move slow and fast by one step until they meet
            slow=slow.next
            fast=fast.next
        return slow                 #the place they meet is the start of the cycle