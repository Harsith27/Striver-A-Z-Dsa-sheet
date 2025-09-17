class SinglyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        curr=self
        ele=[]
        while(curr):
            ele.append(str(curr.val))
            curr=curr.next
        return ' -> '.join(ele)
def create_List(arr):
    head=SinglyNode(arr[0])
    curr=head
    for val in arr[1:]:
        curr.next=SinglyNode(val)
        curr=curr.next
    return head
head=create_List([1,2,3,4,5,6])

#delete at begin
def delete_at_begin(head):
    return head.next
head=delete_at_begin(head)

#delete at end
def delete_at_end(head):
    if head is None:        #empty list
        return head
    if head.next is None:   #list with only one ele
        return None
    curr=head
    while(curr.next.next):
        curr=curr.next
    curr.next=None
    return head
head=delete_at_end(head)


#delete by value
def delete_value(ele,head):
    curr=head
    while curr.next and curr.next.val!=ele:
        curr=curr.next
    if curr.next is not None:
        curr.next=curr.next.next
    return head
head=delete_value(7,head)

#delete at position 
def delete_at_position(pos,head):
    if head is None:
        return head
    if pos==0:
        return head.next
    curr=head
    p=0
    while curr.next and p<pos-1:
        curr=curr.next
        p+=1
    if curr.next is None:
        return head
    curr.next=curr.next.next
    return head
head=delete_at_position(2,head)
