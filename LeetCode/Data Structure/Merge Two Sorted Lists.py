# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def AddValue(self, val=0):

        if self.next == None:
            self.next = ListNode(val)
            return

        NextNode = self.next
        while NextNode.next != None:
            NextNode = NextNode.next

        NextNode.next = ListNode(val)

    def NextNode(self):
        return self.next
    def AddList(self, listNods):
        for item in listNods:
            self.AddValue(item)
    def PrintList(self):
        print(self.val, end = " ")
        NextNode = self.next

        while NextNode != None:
            print(NextNode.val, end = " ")
            NextNode = NextNode.next


        print()





class Solution:
    def mergeTwoLists(self, list1, list2):

        list3 = ListNode()
        FirstNode = list3

        while (list1 != None) or (list2 != None):






            if list1 == None:
                list3.val = list2.val
                list2 = list2.next




            elif list2 == None:
                list3.val = list1.val
                list1 = list1.next



            elif list1.val < list2.val:
                list3.val = list1.val
                list1 = list1.next


            elif list1.val > list2.val:
                list3.val = list2.val
                list2 = list2.next


            elif list1.val == list2.val:
                list3.val = list1.val
                list3.next = ListNode()
                list3 = list3.next

                list3.val = list2.val

                list1 = list1.next
                list2 = list2.next

            if list1 != None or list2 != None:
                list3.next = ListNode()
                list3 = list3.next


        return FirstNode

list1 = ListNode(1)

list1.AddList([500, 1000, 10000])
list1.PrintList()
list2 = ListNode(5)
list2.AddList([10, 15, 99999])
list2.PrintList()

sol = Solution()
list3 = sol.mergeTwoLists(list1, list2)
list3.PrintList()


