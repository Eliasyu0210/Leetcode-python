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
        stack = []
        ans = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right

        return ans
