from collections import Counter


class Solution:
    def __init__(self) -> None:
        pass
    def longestCommonPrefix(self, strs):
        res =""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res = res + strs[0][i]
        return res
if __name__=='__main__':
    k=Solution()
    print(k.longestCommonPrefix(["flow","flight","flower"]))