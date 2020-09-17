class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hash = {}

        for i in strs:
            tmp = [0] * 26
            for j in i:
                tmp[ord(j)-ord('a')] += 1 # 关键语句，以'a'为基点来计数
            if Hash.get(tuple(tmp)) is None:
                Hash[tuple(tmp)] = [i]
            else:
                Hash[tuple(tmp)].append(i)
                
        return list(Hash.values())