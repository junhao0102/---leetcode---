class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = list1
        ptr2 = list2

        head = ListNode()
        current = head

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next

            current = current.next

        if ptr2:
            current.next = ptr2
        else:
            current.next = ptr1

        return head.next
