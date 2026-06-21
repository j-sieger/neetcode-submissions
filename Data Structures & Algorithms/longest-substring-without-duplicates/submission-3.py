class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        l = 0
        maxsubLen = 0
        for i in range(len(s)):    #r=i=righ, l = lege
            if s[i] in lookup:
                l = max(lookup[s[i]]+1, l) # moving l to right
            lookup[s[i]]= i
            maxsubLen = max(maxsubLen, i-l+1)
        return maxsubLen


        