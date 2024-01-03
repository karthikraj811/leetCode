class Solution:
    def mostFrequentEven(self,nums:list[int]) -> int:
        even_nums = set(filter(lambda x: 0 if x%2 else 1,nums))
        if len(even_nums) == 0:
            return -1
        high_count =0 
        for i in even_nums:
            int_count = nums.count(i)
            if int_count > high_count:
                high_count = int_count
                int_val = i
            if int_count == high_count and int_val >i:
                int_val = i
        return int_val
    
nums = [1,3,7,9]    
frq_even = Solution()
print(frq_even.mostFrequentEven(nums))


        

    
        
     





