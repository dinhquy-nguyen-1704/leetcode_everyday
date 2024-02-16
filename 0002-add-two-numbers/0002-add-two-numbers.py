# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from functools import cache
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = []
        @cache
        def transfer_to_list1(x):
            if x is not None:
                list1.append(x.val)
                transfer_to_list1(x.next)

        list2 = []
        @cache
        def transfer_to_list2(x):
            if x is not None:
                list2.append(x.val)
                transfer_to_list2(x.next)   

        transfer_to_list1(l1)
        transfer_to_list2(l2)

        l_new1 = ''.join([str(i) for i in list1])[::-1]
        l_new2 = ''.join([str(i) for i in list2])[::-1]

        ans = int(l_new1) + int(l_new2)
        a = list(str(ans))[::-1]
        b = [int(i) for i in a]
        c = d = ListNode()
        for i in b:
            c.next = ListNode(i)
            c = c.next

        return d.next

        