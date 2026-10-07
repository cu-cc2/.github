class Solution:
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
