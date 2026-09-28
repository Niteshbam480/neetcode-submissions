class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffprod = [1]*len(nums)
        preprod= [1]*len(nums)
        for i in range(1,len(nums)):
            preprod[i]=preprod[i-1]*nums[i-1]
            suffprod[-(i+1)] = suffprod[-(i)] *nums[-(i)]
        for i in range(len(nums)):
            nums[i] = preprod[i]*suffprod[i]
        return nums
