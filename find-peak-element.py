#TC: log(n) 
#SC: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1 #define the right and left pointers
        while l + 1 < r:
            mid = (l + r) // 2 #find the mid
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]: #if the neighbours are lesser than the element, return it
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]: #else check the range (mid-1) to (mid+1) and if mid is in the middle, then move the left ti mid, as there's no peak left side 
                l = mid
            else:
                r = mid ##else  then move the right to mid, as there's no peak right side  

        return r if nums[l] < nums[r] else l #if nothing returns, then print maximum (r,l)