class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_set, t_set = defaultdict(int), defaultdict(int)

            for i, j in zip(s, t): 
                s_set[i] += 1
                t_set[j] += 1
        
        return s_set == t_set
            

        

        return True
