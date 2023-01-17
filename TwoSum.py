class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(0,n):
            for j in range(i+1,n):
                tmp = nums[i]+nums[j]
                if tmp == target:
                    ans.append(i)
                    ans.append(j)
                    break
        

        return ans