# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        curr1 = list1
        curr2 = list2
        head = ListNode()
        prev = head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                curr2 = curr2.next
            prev = prev.next
        if curr2:
            prev.next = curr2
        if curr1:
            prev.next = curr1
        return head.next
