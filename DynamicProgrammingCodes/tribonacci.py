from functools import lru_cache
class Solution:
    @lru_cache(None)
    def tribonacci(self,n:int)->int:
        if n==0:
            return 0
        if n==1 or n ==2 :
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

trib_n = Solution()
print(trib_n.tribonacci(30))


#######  memorised DP #######
class Solution2():
    memo =dict()
    memo[0],memo[1],memo[2]=0,1,1
    def tribonacci(self,n:int)->int:
        if n in self.memo:
            return self.memo[n]
        if n==0:
            return 0
        if n==1 or n ==2 :
            return 1
        self.memo[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.memo[n]

trib_n = Solution2()
print(trib_n.tribonacci(30))