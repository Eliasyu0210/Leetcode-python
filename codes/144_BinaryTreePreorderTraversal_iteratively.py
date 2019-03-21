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
        stack = []
        ans = []
        node = root
        while node or stack:
            if node:
                ans.append(node.val)
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                node = node.right

        return ans
