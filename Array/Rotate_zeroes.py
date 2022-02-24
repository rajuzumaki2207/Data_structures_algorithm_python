class Solution:
    def __init__(self) -> None:
        pass
        
    def moveZeroes(self, nums):
        
        l, r =0 , len(nums)-1
        c=0
        while l<= r:
            if nums[l]==0:
                c= c+1
                nums.pop(l)
                r=r-1
            else:
                l=l+1
        nums.extend([0]*c)

                
                
                
            
                



        return nums



if __name__=="__main__":
    k=Solution()
    
    z=k.moveZeroes([1,0,3,0,5,6,7])
    print (z)