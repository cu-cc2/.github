class Solution:
    def oddEvenList(self, head):
        if not head:
            return
        odd_curr = head
        even_curr = head.next
        even_head = head.next

        while even_curr and even_curr.next:
            odd_curr.next = even_curr.next
            odd_curr = odd_curr.next

            even_curr.next = odd_curr.next
            even_curr = even_curr.next
        
        odd_curr.next = even_head
        return head
