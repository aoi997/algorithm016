class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        a, b = 0, 0
        res = 0
        while a < len(g) and b < len(s):
            if g[a] <= s[b]:
                res += 1
                a += 1
                b += 1
            else:
                b += 1
        return res