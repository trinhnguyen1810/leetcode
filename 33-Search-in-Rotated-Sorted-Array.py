class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0

        while left <= right:
            pivot = left + (right - left) // 2

            if target == nums[pivot]:
                return pivot
                
            if nums[pivot] >= nums[left]:
                if nums[left] <= target and target <= nums[pivot]:
                    right = pivot -1
                else:
                    left = pivot + 1
            else:
                if nums[pivot] <= target and target <= nums[right]:
                    left = pivot +1
                else:
                    right = pivot - 1

        return -1
