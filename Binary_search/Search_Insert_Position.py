class Solution:
    def __init__(self) -> None:
        pass
    def searchInsert(self, nums, target) -> int:
        l, r = 0 , len(nums)-1
        
        while l<= r:
            m= (l+r)//2
           
            if target> nums[m]:
                l=m+1
            elif target < nums[m]:
                r= m-1
            elif target == nums[m]:
                return (m)
       
        return l
        


      

if __name__=="__main__":
    k=Solution()
    z= k.searchInsert([1,3,4,6],7)
    print (z)