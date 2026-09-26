# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head 

        if not head or not head.next:
            return 

        slow, fast = head, head 

        while fast and fast.next:
            slow =slow.next 
            fast = fast.next.next 
        
        

        curr = slow.next 
        prev = None

        slow.next = None 

        while curr:
            dum = curr.next 
            curr.next = prev
            prev = curr 
            curr  =  dum 

        first , second = head, prev 

        while second:
            tmp1, tmp2 = first.next , second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            

            












        