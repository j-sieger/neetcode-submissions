from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    #My soltuions    
        frequency = Counter(nums)        
        sorted_by_frequency = dict(sorted(frequency.items(), key= lambda item:item[1], 
                                reverse = True))        
        return list(sorted_by_frequency.keys())[:k]
        
        