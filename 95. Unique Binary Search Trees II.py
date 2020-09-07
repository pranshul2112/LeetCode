#  https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, arr, res, tree):
        if len(arr) == 0:
            return []
        elif len(arr) == 1:
            return [TreeNode(arr[0])]
        elif len(arr) == 1:
            tree1 = TreeNode(arrp[0])
            tree1.right = TreeNode(arr[1])
            tree2 = TreeNode(arr[1])
            tree2.left = TreeNode(arr[0])
            
            return [tree1, tree2]
        if len(res) != 0:
            res = []
            
        for i in range(len(arr)):
            leftTrees = self.build(arr[0:i], tree[arr[i]]["l"], tree)
            rightTrees = self.build(arr[i+1:len(arr)], tree[arr[i]]["r"], tree)
            
            if len(leftTrees) == 0:
                leftTrees.append(None)
            if len(rightTrees) == 0:
                rightTrees.append(None)
                
            for x in leftTrees:
                for y in rightTrees:
                    nTree = TreeNode(arr[i])
                    nTree.left = x
                    nTree.right = y
                    res.append(nTree)
            
        return res
            
    def generateTrees(self, n: int) -> List[TreeNode]:
        visited = {}
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
            visited[i] = {}
            visited[i]["l"] = []
            visited[i]["r"] = []
        #print(visited)
        return self.build(arr, [], visited)
            
