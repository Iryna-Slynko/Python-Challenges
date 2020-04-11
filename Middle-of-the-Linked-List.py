# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/
#Middle of the Linked List
#Given a non-empty, singly linked list with head node head, return a middle node of linked list.

#If there are two middle nodes, return the second middle node.
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        item = head
        result=head
        counter=0
        
        while item != None and item.next != None:
            item = item.next.next
            result = result.next
            counter+=1

    """
        middle_index=counter//2
        
        item=head
        for i in range(middle_index):
            item=item.next
        return item
        """
