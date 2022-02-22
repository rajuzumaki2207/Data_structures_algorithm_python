import string
class Solution:
    def __init__(self) -> None:
        pass
    def titleToNumber(self, columnTitle: str) -> int:
        temp =dict()
        k=1
        for l in string.ascii_uppercase:
    
            temp[l] = k
            k=k+1
        result=0
        for s in range(len(columnTitle)):
            print (temp[columnTitle[-1-s]])
            result += temp[columnTitle[-1-s]]*(26**s)
        return result
        
        
if __name__=="__main__":
    k=Solution()
    z= k.titleToNumber("AZ")
    print (z)