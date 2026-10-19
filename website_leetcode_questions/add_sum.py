l1 = [2,4,3]
l2 = [5,6,4]


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry:
            d1 = l1.val if l1 is not None else 0
            d2 = l2.val if l2 is not None else 0
            total = d1 + d2 + carry
            d = total % 10
            carry = total // 10
            current.next = ListNode(d)
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next
        return dummy.next



        