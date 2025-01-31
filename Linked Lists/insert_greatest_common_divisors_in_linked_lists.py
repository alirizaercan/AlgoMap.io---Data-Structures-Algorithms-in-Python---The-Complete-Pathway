# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcd = math.gcd(cur.val, prev.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next

        return head

    
    # Time Complexity : O(n*A)
    # Space Complexity : O(1)