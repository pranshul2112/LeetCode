#  https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        def psum(root, s):
            if root == None: 
                return 0
            
            res = 0
            if root.val == s: res += 1
            res += psum(root.left, s - root.val)
            res += psum(root.right, s - root.val)
            return res
        
        if root == None:
            return 0
        return self.pathSum(root.left, s) + psum(root, s) + self.pathSum(root.right, s) 
    
