class Solution:
    def reverseWords(self, s: str) -> str:
       
        return  " ".join(x[::-1] for x in s.split())
        
if __name__=="__main__":
    k=Solution()
    print(k.reverseWords("Let's take LeetCode contest"))