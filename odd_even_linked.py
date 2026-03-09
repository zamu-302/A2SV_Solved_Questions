# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        even=[arr[i] for i in range(len(arr)) if i%2!=0]
        odd=[arr[i] for i in range(len(arr)) if i%2==0]
        dummy=ListNode()
        curr=dummy
        print(even,odd)
        for i in range(len(odd)):
            dummy.val=odd[i]
            dummy.next=ListNode()
            dummy=dummy.next
        for i in range(len(even)):
            dummy.val=even[i]
            if i!=len(even)-1:
                dummy.next=ListNode()
                dummy=dummy.next
        return curr


        