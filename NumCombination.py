class Solution:
    def letterCombinations(self, digits: str):
        d = {
                
                "2": ["a","b","c"],
                "3": ["d","e","f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6" : ["m","n", "o"],
                 "7" : ["p", "q", "r", "s"],
                 "8" : ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]
                }
        res=[]
        def BckTrack (i, cstr):
            if len(cstr)==len(digits):
                res.append(cstr)
                return
            for c in d[digits[i]]:
                 BckTrack(i+1, cstr+c)
        if digits:
             BckTrack(0, "")
        return res


    
if __name__=="__main__":
    k=Solution()
    print(k.letterCombinations("23"))