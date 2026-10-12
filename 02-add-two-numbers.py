# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = ListNode()
        l3_head = l3

        external_overflow = 0

        while l1 != None or l2 != None:
            internal_overflow = 0
            res = (l1.val if l1 else 0) + (l2.val if l2 else 0) + external_overflow
            if res > 9:
                internal_overflow = 1
                res += -10
            l3.val = res
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            external_overflow = internal_overflow

            if l1 is not None or l2 is not None or external_overflow:
                l3.next = ListNode()
                l3 = l3.next
        
        if external_overflow == 1:
            l3.val = external_overflow

        return l3_head
    