class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}
        ans=[]
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff not in summ.keys():
                summ[nums[i]] = i
            else:
                j=summ[diff]
                ans.append(j)
                ans.append(i)
        return ans
                            