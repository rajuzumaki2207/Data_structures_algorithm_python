class Solution:
    def maxArea(self, height: list()) -> int:
        vols = []
        
        l = 0
        r = len(height) - 1

        while l < r:
            
            if height[l] < height[r]:
                vols.append(height[l] * (r-l))
                l += 1

            else:
                vols.append(height[r] * (r-l))
                r -= 1      
                            
        return max(vols)
            


        


if __name__=="__main__":
    k=Solution()

    print (k.maxArea([1,14,6,2,5,4,8,14,15]))