# 144. Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.preorder(root, ans)

        return ans

    def preorder(self, node, ans=[]):
        if node:
            ans.append(node.val)
            self.preorder(node.left, ans)
            self.preorder(node.right, ans)
