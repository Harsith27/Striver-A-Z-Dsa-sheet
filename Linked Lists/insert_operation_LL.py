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


#insert at begin
def Insert_node_at_begin(ele,head):
    new_node=SinglyNode(ele)
    new_node.next=head
    head=new_node
    return head
head=Insert_node_at_begin(8,head)


#insert at end
def Insert_node_at_end(ele,head):
    new_node=SinglyNode(ele)
    if head is None:
        return new_node 
    curr=head
    while(curr.next):
        curr=curr.next
    curr.next=new_node
    return head

head=Insert_node_at_end(11,head)


#insert after given node
def insert_after_given_node(prev_node,ele):
    new_node=SinglyNode(ele)
    new_node.next=prev_node.next
    prev_node.next=new_node

curr=head
while curr and curr.val!=6:
    curr=curr.next

insert_after_given_node(curr,7)


#insert after given value
def insert_after_given_value(val,head,ele):
    curr=head
    while curr and curr.val!=val:
        curr=curr.next
    new_node=SinglyNode(ele)
    new_node.next=curr.next
    curr.next=new_node

insert_after_given_value(8,head,9)

#insert after given pos
def insert_after_given_pos(head,pos,ele):
    new_node=SinglyNode(ele)
    if pos==0:                   #edge case
        new_node.next=head
        return new_node
    p=0
    curr=head
    while curr and (p!=pos):
        curr=curr.next
        p+=1
    new_node.next=curr.next
    curr.next=new_node
    return head
head=insert_after_given_pos(head,8,10)

