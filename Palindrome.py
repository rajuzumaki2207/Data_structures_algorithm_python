from anyio import typed_attribute


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x=list(str(x))
        l, r = 0, len(x)-1
        while l<=r:  
            if x[l] == x[r]:
                z= True
                
                l=l+1
                r=r-1
            else:
                z= False
                break
        return z



        
            
            



if __name__=='__main__':
    k=Solution()
    print(k.isPalindrome(121))