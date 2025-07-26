class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        f={}
        for e in s:
            d[e]=d.get(e,0)+1
        for e in t:
            f[e]=f.get(e,0)+1
        return (d==f)


"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
"""
"""
也可以直接用Counter： cs = Counter(s)
Counter：统计每个元素出现的次数
"""