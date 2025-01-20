           
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        cur_product = 1
        res = 0  
        while r < len(nums):
            cur_product *= nums[r]

            while cur_product >= k and l <= r:
                cur_product /= nums[l]
                l += 1
            res += (r - l + 1)
            r += 1
        return res
