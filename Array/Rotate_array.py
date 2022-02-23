class Solution:
    def __init__(self) -> None:
        pass
        
    def rotate(self, nums: list(), k: int) -> None:
        if (len(nums) == 1) or (k % len(nums)==0):
            pass
        else:
            nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
        return nums
           


        


        

if __name__=="__main__":
    k=Solution()
    
    z=k.rotate([1,2,3,4,5,6,7],3)
    print (z)