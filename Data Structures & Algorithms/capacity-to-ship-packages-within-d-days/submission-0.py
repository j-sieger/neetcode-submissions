class Solution:
    def canShip(self,weights,shipCapacity, targetDays):
        daysCount = 1
        currentLoad = 0
        for weight in weights:
            currentLoad += weight            
            if currentLoad > shipCapacity:
                currentLoad = weight
                daysCount += 1
                if daysCount > targetDays:
                    return False           
        return True #daysCount   

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity = max(weights)
        maxCapacity = sum(weights)
        leastweightCapacity = maxCapacity
        
        while minCapacity <= maxCapacity:
            capacity = (minCapacity + maxCapacity)//2
            daysCount = self.canShip(weights,capacity,days)
            if self.canShip(weights,capacity,days):
                leastweightCapacity = min(leastweightCapacity, capacity)
                maxCapacity = capacity - 1
            else:
                minCapacity = capacity + 1
        return leastweightCapacity
            
