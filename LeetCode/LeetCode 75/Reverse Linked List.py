# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

    def MakeCircle(self, n1, n2):

        count = 0
        Node1 = None
        Node2 = None
        TempNode = self

        while count !=n2 or TempNode != None:

            if count == n1:
                Node1 = TempNode
            elif count == n2:
                Node2 = TempNode
                break

            TempNode = TempNode.next
            count += 1

        Node2.next = Node1



class Solution2:
    def detectCycle1(self, head):



        ListOfNode = []

        CurrNode = head


        while CurrNode != None:

            if CurrNode in ListOfNode:

                return CurrNode

            ListOfNode.append(CurrNode)
            CurrNode = CurrNode.next

        return -1

    def DetectCircle2(self, head):

        fastNode = head
        slowNode = head

        while fastNode == slowNode or fastNode != None:

            slowNode = slowNode.next
            fastNode = fastNode.next.next

        if fastNode == None:
            return  -1
        else:
            fastNode = head
            while fastNode == slowNode:

                slowNode = slowNode.next
                fastNode = fastNode.next
            return slowNode

    def detectCycle3(self, head: ListNode):

        fast, slow = head, head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                slow = head
                while(slow is not fast):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None



list1 = ListNode(1)

list1.AddList([2, 3, 4, 5, 6, 7, 8, 9, 10])
list1.PrintList()
# list2 = ListNode(5)
# list2.AddList([10, 15, 99999])
# list2.PrintList()

list1.MakeCircle(3, 8)
S = Solution2()

Lcircle1 = S.detectCycle1(list1)


print(Lcircle1.val)

Lcircle2 = S.detectCycle3(list1)

print(Lcircle2.val)










