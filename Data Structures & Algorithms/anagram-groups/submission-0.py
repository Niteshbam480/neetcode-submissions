class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            w=''.join(sorted(i))
            group.setdefault(w,[]).append(i)
        ans=[]
        for v in group.values():
            ans.append(v)

        
        return ans
    
    