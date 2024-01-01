class Solution:
    def mincost(self,cost:list[int])->int:
        self.cost = cost
        self.costs =[]
        if self.cost[1] <=self.cost[0]+self.cost[2]:
            self.start = 1
        else:
            self.start = 0
        self.costs = []
        self.costs.append(self.cost[self.start])
        while self.start+2 <len(self.cost):
            if self.cost[self.start]+self.cost[self.start+1] >= self.cost[self.start]+self.cost[self.start+2]:
                self.start = self.start+2
            else:
                self.start = self.start+1
            self.costs.append(self.cost[self.start])
        return sum(self.costs)

min_cost = Solution()
print(min_cost.mincost([0,1,1,1]))


