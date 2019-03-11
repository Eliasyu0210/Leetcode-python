#701. Insert into a Binary Search Tree

# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


# Binary search tree insert
# 1. If the head = None, the to be inserted value should be inserted to the head
# 2. to make sure if the head.left and head.right are valid. means unequal to None.
# 3. if not then using recursive to move the head to left or right.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        else:
            n = root
            while n:
                if n.val > val:
                    if n.left == None:
                        n.left = TreeNode(val)
                        return root
                    else:
                        n = n.left
                else:
                    if n.right == None:
                        n.right = TreeNode(val)
                        return root
                    else:
                        n = n.right
