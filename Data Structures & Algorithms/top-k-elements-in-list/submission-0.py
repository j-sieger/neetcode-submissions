from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)        
        sorted_by_frequency = dict(sorted(frequency.items(), key= lambda item:item[1], 
                                reverse = True))
        print(sorted_by_frequency)
        return list(sorted_by_frequency.keys())[:k]
        
        