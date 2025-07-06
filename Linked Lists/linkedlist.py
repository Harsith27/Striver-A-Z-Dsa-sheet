class SinglyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(head):
        curr=head
        ele=[]
        while curr:
            ele.append(str(curr.val))
            curr=curr.next
        return ' -> '.join(ele)
def create_list(values):
    head=SinglyNode(values[0])
    curr=head
    for val in values[1:]:
        curr.next=SinglyNode(val)
        curr=curr.next
    return head

def reverse_of_a_list(head):
    prev=None
    curr=head
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

def merge_lists(head1,head2):
    curr=head1
    while curr:
        if curr.next == None:
            curr.next=head2
            return
    

        

values1=list(map(int,input().split()))
values2=list(map(int,input().split()))
head1=create_list(values1)
head2=create_list(values2)
merge_lists(head1,head2)
print(head1)