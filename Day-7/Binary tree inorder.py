# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        self.inorder(root,result)
        return result
    def inorder(self,root,result): 
        if(root==None):
            return
        self.inorder(root.left,result)
        result.append(root.val)
        self.inorder(root.right,result)