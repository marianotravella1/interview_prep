"""
LeetCode Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/description/?language=Python

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        
        carry = 0  
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sumcha = v1 + v2 + carry
            
            carry = sumcha // 10
            
            value = sumcha % 10
            
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
    
if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))  
    l2 = ListNode(5, ListNode(6, ListNode(4)))  
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None") 