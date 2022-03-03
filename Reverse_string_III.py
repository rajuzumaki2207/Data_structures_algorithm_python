class Solution:
    def reverseWords(self, s: str) -> str:
        k= s[::-1].split(" ")
        ss=str()
        for i in reversed(range(len(k))):
            if i!=0:
                ss= ss+ k[i] + " "
            else:
                ss= ss+ k[i]

        return  ss
if __name__=="__main__":
    k=Solution()
    print(k.reverseWords("Let's take LeetCode contest"))