class Solution:
    def reverse(self, x: int) -> int:
        if x <0 :
            self.x = str(x)[1:]
            self.x = self.x[::-1]
            self.rev_x = int('-'+self.x)
            if self.rev_x > -2**31   :
                return int(self.rev_x)
            return 0
        self.pos_x = str(x)[::-1]
        if int(self.pos_x) < (2**31)-1:
            return int(self.pos_x)
        return 0
    

obj = Solution()
res = obj.reverse(-120)
print(res)



