class Solution:
    def twoSum(self, numbers: list(), target: int):
        l,r =0 , len(numbers)-1
        
        while l<r:
            temp= numbers[l]+numbers[r]
            
            if temp==target:
                
                return  ([l,r])
                break
            elif target> temp:
                l=l+1
            else:
                r=r-1


            

        return (idx)


if __name__=="__main__":
    k=Solution()
    print (k.twoSum([2,7,11,15],9))