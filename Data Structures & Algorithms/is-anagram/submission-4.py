class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        ms = {}
        mt = {}
        for i in range(len(s)):
            ms[s[i]] = ms.get(s[i], 0) + 1            
            mt[t[i]] = mt.get(t[i], 0) + 1                    
        return ms==mt
        # s_list = list(s)    
        # t_list = list(t)
        # for char in t:            
        #     if char in s_list:
        #         s_list.remove(char)
        #         t_list.remove(char)        
        # if s_list and t_list:
        #     return False
        # return True
        