class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1

        max_num=max(freq.values())
        arr = [[] for _ in range(max_num+1)]

        for key in freq.keys():
            arr[freq[key]].append(key)
        
        res = []
        for i in range(max_num, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res