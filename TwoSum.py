class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        numdict = {}
        for i in range(0,n):
            if (target - nums[i]) in numdict:
                return [ i , numdict[ target - nums[i] ] ]
            else:
                numdict[ nums[i] ] = i