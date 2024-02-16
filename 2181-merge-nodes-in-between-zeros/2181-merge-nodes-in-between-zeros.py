# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        k = new_list = ListNode()
        while head.next:
            tmp = head.next
            c = 0
            while tmp.val != 0:
                c += tmp.val
                tmp = tmp.next
            new_list.next = ListNode(c)
            new_list = new_list.next
            head = tmp

        return k.next
        