# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result=[]
        self.preorder(root,result)
        return result
    def preorder(self,root,result): 
        if(root==None):
            return
        result.append(root.val)
        self.preorder(root.left,result)
        self.preorder(root.right,result)