class Solution:
    def countCycle(head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break               #1.normal cycle detection
        else:
            return None 
        count=1
        fast=fast.next                
        while(slow!=fast):          
            fast=fast.next
            count+=1
        return count      
    