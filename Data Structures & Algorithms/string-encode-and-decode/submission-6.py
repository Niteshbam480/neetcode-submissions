class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + "`"+ i
        return res
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        res = []
        strs = s.split("`")
        strs.pop(0)
        for i in strs:
            res.append(i)
        return res