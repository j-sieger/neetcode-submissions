class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_list = list(s)    
        t_list = list(t)
        for char in t:            
            if char in s_list:
                s_list.remove(char)
                t_list.remove(char)        
        if s_list and t_list:
            return False
        return True
        