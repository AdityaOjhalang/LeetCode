class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left,right = 0,len(nums) - 1

        while left <= right:
            mid = (left + right)//2


            if nums[mid]  == target:
                return mid 
            
            #left is sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 

            #go right
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid -1
        return -1