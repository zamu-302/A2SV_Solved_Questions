# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr=[]
        while head:
            
            arr.append(head.val)
            head=head.next
        arr.reverse()
        new_node=ListNode()
        curr=new_node
        for i in range(len(arr)):
            curr.val=arr[i]
            if i!=len(arr)-1:
                curr.next=ListNode()
                curr=curr.next
        return new_node