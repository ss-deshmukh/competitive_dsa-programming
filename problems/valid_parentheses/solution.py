class Solution:
    def isValid(self, s: str) -> bool:
        
        stringList = list(s)
        bracDict = {'(':')', '[':']', '{':'}'}
        stack = []

        for char in stringList:
            if char in bracDict:
                stack.append(char)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if bracDict[check] != char:
                    return False
        return len(stack)==0