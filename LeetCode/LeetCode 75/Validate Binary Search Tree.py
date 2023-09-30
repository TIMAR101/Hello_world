import collections as cl
import math
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

        print(q)

        print(output)

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
                node =queue.popleft()

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
    def inOrder(self):
        arr = []
        def inorder(node):
            if node is None: return None
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(self)
        return arr

    def isValid(self):

        listTree = self.printList2()

        heighTree = len(listTree)

        high = 0
        # 0-0, 1-1, 2-3 -2, 4-7 - 3, 8-15 -4

        #heighTree = math.floor(math.log(lenTree, 2) + 1)


        for level in range(len(heighTree)):
            pass

            for levelnum in range(len(level)):
                pass

                #if listTree[level][levelnum] > max(listTree[le])








            for item2 in range(len(listTree)):
                pass












class Solution:
    def isValidBST(self, root) -> bool:

        queue = cl.deque([[root, None, None]])







        while queue:

           for _ in range(len(queue)):
                node = queue.popleft()



                if node[0].left != None:
                    if node[0].left.val >= node[0].val:
                        return False
                    if node[2] == "RIGHT":
                        if node[0].left.val <= node[1]:
                            return False

                    queue.append([node[0].left, node[0].val, "LEFT"])

                if  node[0].right != None:
                     if node[0].right.val <= node[0].val:
                         return False
                     if node[2] == "LEFT":
                        if node[0].right.val >= node[1]:
                            return False

                     queue.append([node[0].right, node[0].val, "RIGHT"])

        return True

Tree1 =  [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]


print(Tree1)
TreeNode1 = TreeNode(120)

for item in Tree1[1:]:
    TreeNode1.add(item)



# TreeNode1.add(6)
# TreeNode1.add(7)
# TreeNode1.add(8)

print(TreeNode1.print())

print(TreeNode1.printList())

print(TreeNode1.printList2())

print(TreeNode1.Recprint())

S1 = Solution()

print(S1.isValidBST(TreeNode1))

print(math.floor(math.log(3, 2) + 1))

print(TreeNode1.inOrder())
