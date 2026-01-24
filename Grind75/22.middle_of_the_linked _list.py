# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head

        if head.next:
            fast = head.next
        else:
            return head

        while fast.next and fast.next.next:
            if fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = fast.next
                slow = slow.next

        return slow
