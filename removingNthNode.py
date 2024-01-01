class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printElement(self):
        next = self.next
        val = self.val
        print(val)
        while next:
            print(next.val)
            next = next.next



class Solution:  
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head




LinkedList = ListNode(val = 20,next = ListNode(val = 12,next =ListNode(val = 1,next=ListNode(val=7,next=ListNode(13,ListNode(27,None))))))

sol = Solution()
sol.removeNthFromEnd(head=LinkedList,n=6).printElement()

