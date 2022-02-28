class Solution:
    def __init__(self) -> None:
        pass
    def summaryRanges(nums: list()):
        ans, i = [], 0                # take i to traverse the array, ans to fill the ranges
        while i < len(nums):          # traverse the array
            lower = upper = nums[i]   # for a range we need to find the upper and lower values
            while i < len(nums) and nums[i] == upper:  # increment the i and upper as well in order to check they are equal.
                i += 1
                upper += 1
            ans.append(str(lower) + ("->" + str(upper-1) if upper-lower-1 else ""))  # if upper-1 and lower both are equal append only lower, else append the range
        return ans
if __name__=="__main__":
    k=Solution.summaryRanges([0,1,2,3,4,6,7])
    print (k)