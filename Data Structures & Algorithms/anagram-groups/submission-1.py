class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # My both the solutions are optimal
    # sol 1:
        result = defaultdict(list)        
        for s in strs:
            sortedS = ''.join(sorted(s)) #sorted returns list of chars so joining it back to make word again
            result[sortedS].append(s)        
        return list(result.values())

    #sol 2:    
        # list_annograms = []
        # already_looked_strs=[]
        # for i in range(len(strs)):  
        #     if strs[i] in already_looked_strs:
        #         continue
        #     annograms = []
        #     annograms.append(strs[i])            
        #     for j in range(i+1, len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             annograms.append(strs[j])
        #             already_looked_strs.append(strs[j])
        #     list_annograms.append(annograms)
        
        # return list_annograms