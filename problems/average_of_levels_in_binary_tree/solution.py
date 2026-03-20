# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        que = deque([root])
        result = []
        
        while que:
                
            avg = 0
            next_que = deque()
            count = 0
            for node in que:
                avg += node.val
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
                count +=1
                
            que = next_que
            result.append(avg/count)
        
        return(result)
        

            