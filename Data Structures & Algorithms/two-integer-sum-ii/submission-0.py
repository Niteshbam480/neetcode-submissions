class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<len(numbers) and j<len(numbers):
            sum = numbers[i]+numbers[j]
            if sum == target:
                break
            elif sum<target:
                i+=1
            else:
                j-=1
        return [i+1,j+1]