'''
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
 
P     I    N
A   L S  I G
Y A   H R
P     I

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

P   A   H   N
A P L S I I G
Y   I   R

Input: s = "A", numRows = 1
Output: "A"
'''





class Solution:
     def convert(self,s,numRows):
        self.s = s
        self.rows = numRows
        self.inc = self.rows + (self.rows-2)
        self.fin_str =''
        if len(s) <= self.rows or len(self.s)==2 or len(self.s)==1 or self.rows==1:
            return s
        for i in range(1,self.rows+1):
            if i == 1 or i == self.rows:
                while True:
                    self.fin_str = self.fin_str + self.s[i-1]
                    i = i +self.inc            
                    if i > len(self.s):
                        break
            else:
                start = i
                next = i + (self.rows + (self.rows- 2*i))
                while True:
                    self.fin_str = self.fin_str + self.s[start-1]
                    start = start +self.inc            
                    if next > len(s):
                        break
                    self.fin_str = self.fin_str + self.s[next-1]
                    next = next +self.inc
                    if start > len(s):
                        break

        return self.fin_str
 
obj = Solution()
res1 =obj.convert('PAYPALISHIRING',3)
res2 =obj.convert('PAYPALISHIRING',4)
res3 =obj.convert('A',1)
print(res1=="PAHNAPLSIIGYIR"," ",res2=="PINALSIGYAHRPI"," ",res3=="A")
            

            
            
         




