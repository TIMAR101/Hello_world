"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        :type root: Node
        :rtype: List[int]
        """

        output =[]

        # perform dfs on the root and get the output stack
        self.dfs(root, output)

        # return the output of all the nodes.
        return output

    def dfs(self, root, output):

        # If root is none return
        if root is None:
            return

        # for preorder we first add the root val
        output.append(root.val)

        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, output)

    def preorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        output = []

        # Till there is element in stack the loop runs.
        while stack:

            #pop the last element from the stack and store it into temp.
            temp = stack.pop()

            # append. the value of temp to output
            output.append(temp.val)

            #add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(temp.children[::-1])

        #return the output
        return output

class Solution1(object):
    def preorder(self, root):
        # To store the output result...
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        # Base case: If root is none...
        if root is None: return
        # Append the value of the root node to the output...
        output.append(root.val)
        # Recursively traverse each node in the children array...
        for child in root.children:
            self.traverse(child, output)
