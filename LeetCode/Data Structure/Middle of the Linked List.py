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


class Solution:
    def middleNode(self, head: ListNode):

        if head == None:
            return -1

        if head.next == None:
            return head

        ListofNode=[]
        HeadNode = head
        TempNode = head
        #TempNode, HeadNode = head


        while TempNode != None:

            ListofNode.append(TempNode)
            TempNode = TempNode.next

            # PartLen = len(ListofNode) % 2


        return ListofNode[len(ListofNode) // 2]

def middleNode1(self, head):
	a = []
	while head:
		a.append(head)
		head = head.next
	return a[len(a)//2]

class Solution2:
    
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

L1 = ListNode(1)

L1.AddList([2,3,4,5,6])
L1.PrintList()

S1 = Solution()
L2 = S1.middleNode(L1)
print()

L2.PrintList()



