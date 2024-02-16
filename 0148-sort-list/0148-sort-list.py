# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = []

        while head:
            temp.append(head.val)
            head = head.next

        temp.sort()

        if temp:

            a = ListNode(temp[0])

            b = a

            for i in temp[1:]:
                a.next = ListNode(i)
                a = a.next

            return b

        else:

            return head
        