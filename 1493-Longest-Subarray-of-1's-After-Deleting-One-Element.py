class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      """
      [0,1,1,1,0,1,1,0,1]
      l = 0 
      k = 1
      res = 0
      max_res = 
      for i in range(len(nums)):
        if nums[i] = 0:
          k -= 1
        else:
          res += 1
          
        while k < 0 and l <= r:
          if nums[l] == 0:
            k += 1
          else:
            res -= 1
          l += 1
        
        max_res = max(res, max_res)
      return max res
      """
      l = 0
      k = 1
      max_res = 0
      for r in range (len(nums)):
        if nums[r] == 0:
          k-= 1

        while k < 0 and l <= r:
          if nums[l] == 0:
            k += 1
          l += 1
        
        max_res = max(max_res, r - l)
        
      return max_res


