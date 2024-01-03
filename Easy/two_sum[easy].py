import sys
# sys.setrecursionlimit(100000)
def twoSum(nums: list[int], target: int) -> list[int]:
    nums = nums
    target = target
    def sum_rec(start,next):
        if next == len(nums):
            start = start+1
            next = start+1
        if (nums[start]+nums[next]) == target:
                return [start,next]
        else:
            next = next+1
            return sum_rec(start,next)
    return sum_rec(0,1)

nums = [1,2,3,4]
target = 5
print(twoSum(nums,target))



     










