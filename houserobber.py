#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[len(nums)-1]
            
