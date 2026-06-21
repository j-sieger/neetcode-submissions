class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        hash_map = {}
        if len(s_list) == len(pattern):
            for i in range(len(s_list)):
                value = hash_map.get(pattern[i], None)
                if value: 
                    if s_list[i]==value:
                        continue
                    else:
                        return False
                elif s_list[i] in s_list[:i]:
                    return False
                hash_map[pattern[i]]=s_list[i]
            return True
        else: 
            return False

            
        