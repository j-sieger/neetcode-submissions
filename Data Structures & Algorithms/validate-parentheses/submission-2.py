class Solution:
    def isValid(self, s: str) -> bool:        
        parathesis_map = {"}":"{","]":"[",")":"("}
        stack = []
        for i, p in enumerate(s):            
            if p in "[{(":
                stack.append(p)            
            elif p in ")}]" and stack and stack[-1] == parathesis_map[p]:
                stack.pop(-1) #or below line also works                
            else:
                return False           
        if not stack:
            return True
        return False

        