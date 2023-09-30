import collections as cl
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, val):



        queue = [self]

        next_queue = []
        level = []
        result = []
        node = self

        while queue:

            for node in queue:
                if node.left == None:
                    node.left = TreeNode(val)
                    queue = []
                    next_queue = []

                    break
                elif node.right == None:

                    node.right = TreeNode(val)
                    queue = []
                    next_queue = []
                    break

                else:
                    next_queue.append(node.left)
                    next_queue.append(node.right)

            queue = next_queue.copy()
            next_queue.clear()

    def print(self):
        queue = [self]


        next_queue = []
        level = []
        result = []
        result.append(self.val)
        node = self

        while queue:

            for node in queue:
                if node.left != None:
                    result.append(node.left.val)
                    next_queue.append(node.left)

                if node.right != None:

                    result.append(node.right.val)
                    next_queue.append(node.right)



            queue = next_queue.copy()
            next_queue.clear()



        return result

    def printList(self):

        queue = cl.deque
        next_queue = cl.deque
        finresult = cl.deque
        result = cl.deque


        queue = [self]


        next_queue = []
        level = []
        finresult = []
        result = []

        result.append(self.val)
        finresult.append(result)
        result = []
        node = self

        while queue:

            for node in queue:
                if node.left != None:
                    result.append(node.left.val)
                    next_queue.append(node.left)

                if node.right != None:

                    result.append(node.right.val)
                    next_queue.append(node.right)



            queue = next_queue.copy()
            next_queue.clear()
            if result:
                finresult.append(result)
            result = []



        return finresult


    def printList2(self):

        q, output = cl.deque([self]),[]

        # print(q)
        #
        # print(output)

        queue = cl.deque
        next_queue = cl.deque
        finresult = cl.deque
        result = cl.deque

        queue = cl.deque([self])

        next_queue = []
        level = []
        finresult = []
        result = []

        #result.append(self.val)
        #finresult.append(result)
        #result = []
        node = self

        while queue:

           for _ in range(len(queue)):
                node = queue.popleft()

                result.append(node.val)
                if node.left != None:

                    queue.append(node.left)

                if node.right != None:

                    queue.append(node.right)

           finresult.append(result)
           result = []





        return finresult

    def Recprint(self):

        global ans
        ans = []
        def bfs(curr = self, level = 0):


            if curr:
                if len(ans) > level:
                    ans[level].append(curr.val)
                else:
                    ans.append([curr.val])
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)
            return
        bfs()
        return ans

    def rightside(self):

        queue = [self]


        next_queue = []

        finresult = []
        result = []

        result.append(self.val)
        finresult.append(result)
        result = []


        while queue:

            for node in queue:
                if node.left != None:
                    result.append(node.left.val)
                    next_queue.append(node.left)

                if node.right != None:

                    result.append(node.right.val)
                    next_queue.append(node.right)



            queue = next_queue.copy()
            next_queue.clear()
            if result:
                finresult.append(result[-1])
            result = []



        return finresult










        """if not root:
            return []
        
        queue = [root]
        next_queue = []
        level = []
        result = []
        
        while queue:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []"""



# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#
#         TreeNodeList = []
#
#         if root == None:
#             return None
#
#         Level = 0
#
#         TreNodeLilst[Level] = root.value
#
#
#         def Traverse(node1, list1, level):
#
#
#
#             level +=1
#
#             if node1.left != None:
#
#                 List1[level] = node1.left.val
#
#                 Traverse(node1.left, list1, level)
#
#             if node1.right != None:
#
#                 List1[level] = node1.right.val
#
#                 Traverse(node1.right, list1, level)
#
#             return
#
#         Traverse(root, list1, level)
#
#         return list1


TreeNode1 = TreeNode(1)
TreeNode1.add(2)

TreeNode1.add(3)
TreeNode1.add(4)
TreeNode1.add(5)
TreeNode1.add(6)
TreeNode1.add(7)
TreeNode1.add(8)


print("TreeNode1.print()")

print(TreeNode1.print())

print("TreeNode1.printList()")

print(TreeNode1.printList())

print("TreeNode1.printList2()")

print(TreeNode1.printList2())

print("TreeNode1.Recprint()")

print(TreeNode1.Recprint())

print(TreeNode1.rightside())

# tempList = [1, 2, 3, 4, 5]
#
# for item in tempList:
#
#     print(item)
#     tempList.clear()
#     tempList = [9, 8, 7]


q=cl.deque()

print(q)
print(type(q))

# a = None
# a.left = 1


