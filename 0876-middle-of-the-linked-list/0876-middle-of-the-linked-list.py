# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        tmp = head
        while tmp is not None:
            l.append(tmp.val)
            tmp = tmp.next

        x = len(l)//2
        for i in range(x):
            head = head .next

        return head
