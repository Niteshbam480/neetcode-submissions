class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        while i<=j:
            h=min(heights[i],heights[j])
            l=abs(j-i)
            max_area=max(max_area,h*l)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_area