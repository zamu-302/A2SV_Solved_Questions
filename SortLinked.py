# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        new_node=ListNode()
        dummy=new_node

        for i in range(len(arr)):
            dummy.val=arr[i]
            if i!=len(arr)-1:
                dummy.next=ListNode()
                dummy=dummy.next
        return new_node        