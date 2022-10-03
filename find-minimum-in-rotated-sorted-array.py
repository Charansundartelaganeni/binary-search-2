#TC: log(n) 
#SC: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        l,r = 0, len(nums)-1 #define the left and right pointer 
        
        while l < r:
            m = (l+r)//2 #find the mid
            if nums[m] >= nums[r]: #find the deviation point where mid is greater than right, that's where you find the minimum
                l = m + 1 #if satisfies, move the left pointer to mid + 1 
            else:
                r = m #else, move the right pointer to mid
        return nums[l] #now the left pointer points to the minimum value