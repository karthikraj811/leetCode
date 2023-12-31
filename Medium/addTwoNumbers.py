# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # def returnNodeAndCarry(self,l1Next,l2Next,carry):
    #     while True:
    #         if l1Next:
    #             int1 = l1Next.val if l1Next.next is None else 0
    #             l1Next = l1Next.next
    #         if l2Next:
    #             int2 = l2Next.val if l2Next.next is  None else 0
    #             l2Next = l2Next.next
            

    #         if l1Next is None and l2Next is None:
    #             break
    #     sum = int1 + int2 + carry
    #     Node = sum if sum<10 else sum%10
    #     carry = carry +sum//10 
    #     return Node,carry
        


    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy



        carry = 0

        while l1 is not None or l2 is not None or carry!=0:

            int1 = l1.val if l1 is not None else 0
            int2 = l2.val if l2 is not None else 0

            sum = int1+int2+carry
            n = sum % 10
            carry = sum // 10

            Node = ListNode(n)

            tail.next = Node
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            



        result = dummy.next
        return result
    
       

    
l1 = ListNode(1,ListNode(0,ListNode(8,None)))
l2 = ListNode(1,ListNode(0,ListNode(4,None)))

sol = Solution()
print(sol.addTwoNumbers(l1,l2).next.next.val)
    

        

            



