https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        hmap = dict()
        inorder = sorted(preorder)
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        #print(hmap)
        def helper(pre, pbeg, pend, ino, ibeg, iend):
            
            if pbeg > pend:  return None
        
            if pbeg == pend:  return TreeNode(pre[pbeg])
            
            rootnode = TreeNode(pre[pbeg])
            rootindex = hmap[pre[pbeg]]
            num = rootindex - ibeg
            
            rootnode.left = helper(pre, pbeg + 1, pbeg + num, ino, ibeg, rootindex -1)
            rootnode.right = helper(pre, pbeg +1 + num, pend, ino, rootindex + 1, iend)
            
            return rootnode
            
        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(preorder) - 1)
        
