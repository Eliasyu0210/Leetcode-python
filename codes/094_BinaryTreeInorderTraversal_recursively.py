# 94. Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, node, ans):
        if node:
            self.inorder(node.left, ans)
            ans.append(node.val)
            self.inorder(node.right, ans)
