class ListNode:
    def __init__(self, val=0, next=None):
        self.values = val
        self.next = next
class Solution:
    def split(self, head):
        if head is None or head.next is None:
            return head, None

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return head, mid

    def merge(self, left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        current.next = left or right

        return dummy.next

    def sortList(self, head):
        if head is None or head.next is None:
            return head

        left, right = self.split(head)

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)