class Solution:
    def __init__(self) -> None:
        pass
    def search(self, nums, target) -> int:
        l,r = 0 , len(nums)-1

        
       

        while l<=r :
            m= (l+r)//2
            
            if nums[m] ==target:
                return m
            elif  target > nums[m]:
                l=m+1
                
                
            elif  target < nums[m]:
                r=m-1

        return l    
                
            



       


if __name__=="__main__":
    l= [1,3,4,5,6,7]
    t= 6
    k= Solution()
    z= k.search(l, t)
    print (z)