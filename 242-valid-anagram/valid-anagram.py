class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_set, t_set = defaultdict(int), defaultdict(int)

            for i in s: s_set[i] += 1
            for i in t: t_set[i] += 1
        
        return s_set == t_set
            

        

        return True
