# 145. Binary Tree Postorder Traversal

# Given a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.postOrder(root, ans)
        return ans

    def postOrder(self, node, ans):
        if node:
            self.postOrder(node.left, ans)
            self.postOrder(node.right, ans)
            ans.append(node.val)
