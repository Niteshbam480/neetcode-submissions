class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        lenn=1
        maxLen = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                lenn+=1
            elif nums[i]!=nums[i-1] and nums[i]!=nums[i-1]+1:
                lenn=1
            maxLen = max(maxLen,lenn)
        
        return maxLen