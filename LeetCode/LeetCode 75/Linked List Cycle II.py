# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:



        ListOfNode = []

        CurrNode = head


        while CurrNode != None:

            if CurrNode in ListOfNode:

                return CurrNode

            ListOfNode.append(CurrNode)
            CurrNode = CurrNode.next

        return -1
