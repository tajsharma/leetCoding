from logging.config import valid_ident



class treeNode:
    self.val = val
    self.left = left
    self.right = right
    
#LC 100: Same Tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  #base case returns true if both are empty
            return True
        if not p or not q or p.val !=q.val: #2nd base case returns false if either one doesnt exist
            return False                    #or if they are not equall to eachother
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        #^ recursive step; function call on both left and right sides of each tree until base case is reached