class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i,0)+1
        for k,v in frequency.items():
            if v>1:
                return True
        return False
        