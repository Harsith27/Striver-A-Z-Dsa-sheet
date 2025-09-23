def reverse_LL(head):
    curr=head
    prev=None
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=curr.next
    return prev