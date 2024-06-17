class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        mid = 0

        while low <= high:

            mid =  (high + low) // 2

            if target < nums[mid]:
                high = mid - 1
            
            elif target > nums[mid]:
                low = mid + 1

            else:
                return mid
        
        return -1 
